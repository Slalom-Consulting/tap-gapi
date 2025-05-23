"""gapi tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_gapi import streams

class Tapgapi(Tap):
    """gapi tap class."""

    name = "tap-gapi"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            secret=True,
            description="The client id to receive a bearer token from the API service",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            secret=True,
            description="The client secret to receive a bearer token from the API service",
        ),
        th.Property(
            "scope",
            th.StringType,
            required=True,
            description="The API scope that will be used by the tap",
        ),
        th.Property(
            "grant_type",
            th.StringType,
            required=True,
            description="The grant type that will be used by the tap for authentication",
        ),
        th.Property(
            "url_base",
            th.StringType,
            required=True,
            description="The url base for the request",
        ),
        th.Property(
            "access_token_url",
            th.StringType,
            required=True,
            description="URL that the tap will send the client credentials to to receive a bearer token",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.gapiStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        tap_scope = self.config["scope"]
        if tap_scope == 'finance/coa':
            selected_streams = [
            streams.FinanceCOAOrganizationStream(self),
            streams.FinanceCOAFunctionStream(self),
            streams.FinanceCOACostCenterStream(self),
            streams.FinanceCOALegalEntityStream(self),
            streams.FinanceCOAGeographyStream(self),
            ]
        elif tap_scope == 'business/taxonomy':
            selected_streams = [
            streams.BusinessTaxonomyMarketsStream(self),
            streams.BusinessTaxonomyCapabilitiesStream(self),
            streams.BusinessTaxonomySubcapabilitiesStream(self),
            streams.BusinessTaxonomyGroupsStream(self),
            streams.BusinessTaxonomyTaxonomyTypesStream(self),
            streams.BusinessTaxonomyTaxonomyTypesCapabilities(self),
            streams.BusinessTaxonomyTaxonomyTypesIndustriesStream(self),
            streams.BusinessTaxonomyTaxonomyTypesCustomerOutcomesStream(self),
            streams.BusinessTaxonomyTaxonomyTypesGoToMarketStream(self),
            streams.BusinessTaxonomyTaxonomyTypesSlalomGeographyStream(self),
            streams.BusinessTaxonomyLocationsStream(self),
            streams.BusinessTaxonomyTaxonomyTypesSGAStream(self),
            streams.BusinessTaxonomyTaxonomyTypesCustomersStream(self),
            ]
        else:
            selected_streams = []

        return selected_streams 


if __name__ == "__main__":
    Tapgapi.cli()
