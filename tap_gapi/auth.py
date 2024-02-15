"""gapi Authentication."""

from __future__ import annotations

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


# The SingletonMeta metaclass makes your streams reuse the same authenticator instance.
# If this behaviour interferes with your use-case, you can remove the metaclass.
class gapiAuthenticator(OAuthAuthenticator):
    """Authenticator class for gapi."""

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the AutomaticTestTap API.

        Returns:
            A dict with the request body
        """
        # TODO: Define the request body needed for the API.
        return {
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
            "grant_type": self.config["grant_type"],
            "access_token_url": self.config["access_token_url"],
            "scope": "business/taxonomy",
        }

    @classmethod
    def create_for_stream(cls, stream) -> gapiAuthenticator:  # noqa: ANN001
        """Instantiate an authenticator for a specific Singer stream.

        Args:
            stream: The Singer stream instance.

        Returns:
            A new authenticator.
        """
        return cls(
            stream=stream,
            auth_endpoint= stream.config["access_token_url"],
            oauth_scopes= stream.config["scope"],
        )
