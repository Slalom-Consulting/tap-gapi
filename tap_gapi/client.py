"""REST client handling, including gapiStream base class."""

from __future__ import annotations

import json
import urllib.parse
import sys
from functools import cached_property
from typing import Any, Callable, Iterable

import requests
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import JSONPathPaginator # noqa: TCH002
from singer_sdk.streams import RESTStream

from tap_gapi.auth import gapiAuthenticator

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]

class gapiStream(RESTStream):
    """gapi stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config.get("url_base")

    records_jsonpath = "$.result[*]"

    @cached_property
    def authenticator(self) -> _Auth:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return gapiAuthenticator.create_for_stream(self)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        headers["correlation-object"] = '{"correlationId":"dataplatform"}'
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {}
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

class gapiPaginator(JSONPathPaginator):
    """gapi paginator class."""

    def get_next(self, response: requests.Response) -> Any | None:
        """Return a token for identifying the next page of results."""
        last_evaluated_key = extract_jsonpath(self._jsonpath, response.json())
        return next(last_evaluated_key, None)

class paginatedGapiStream(gapiStream):
    """gapi paginated stream class."""

    def get_new_paginator(self):
        return gapiPaginator(jsonpath=self.last_evaluated_key_jsonpath)
    
    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config.get("url_base")

    last_evaluated_key_jsonpath = "$.result.lastEvaluatedKey"
    records_jsonpath = "$.result.items[*]"


    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {"activeStatus": "ALL"}
        if next_page_token:
            next_token = urllib.parse.quote(json.dumps(next_page_token))
            params["nextToken"] = next_token
        return params