from atlassian import Jira
from .base import TicketProvider


class JiraProvider(TicketProvider):
    """Jira ticket provider implementation."""

    def __init__(self, config: dict):
        """
        Initialize Jira provider with configuration.

        Args:
            config: Dictionary containing 'url', 'username', and 'token'
        """
        self.jira = Jira(
            url=config["url"], username=config["username"], password=config["token"]
        )

    def get_ticket_title(self, ticket_id: str) -> str:
        """
        Fetch Jira ticket summary.

        Args:
            ticket_id: The Jira ticket number (e.g., 'ADA-1234')

        Returns:
            The ticket summary as a string

        Raises:
            Exception: If the ticket cannot be found or API call fails
        """
        issue = self.jira.issue(ticket_id)
        return issue["fields"]["summary"]

    @staticmethod
    def get_platform_name() -> str:
        """Return the platform name."""
        return "Jira"
