import requests
from main.providers.base import TicketProvider


class LinearProvider(TicketProvider):
    """Linear issue provider implementation using GraphQL API."""

    GRAPHQL_ENDPOINT = "https://api.linear.app/graphql"

    def __init__(self, config: dict):
        """
        Initialize Linear provider with configuration.

        Args:
            config: Dictionary containing 'api_key'
        """
        self.api_key = config["api_key"]
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key,
        }

    def get_ticket_title(self, ticket_id: str) -> str:
        """
        Fetch Linear issue title using GraphQL API.

        Args:
            ticket_id: The Linear issue identifier (e.g., 'ADA-1234')

        Returns:
            The issue title as a string

        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If the Linear API returns an error
            KeyError: If the response doesn't contain expected data
        """
        query = """
        query GetIssue($id: String!) {
          issue(id: $id) {
            title
          }
        }
        """

        response = requests.post(
            self.GRAPHQL_ENDPOINT,
            json={"query": query, "variables": {"id": ticket_id}},
            headers=self.headers,
            timeout=30,
        )

        response.raise_for_status()
        data = response.json()

        if "errors" in data:
            error_messages = [error.get("message", str(error)) for error in data["errors"]]
            raise ValueError(f"Linear API error: {', '.join(error_messages)}")

        return data["data"]["issue"]["title"]

    @staticmethod
    def get_platform_name() -> str:
        """Return the platform name."""
        return "Linear"
