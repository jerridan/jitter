from abc import ABC, abstractmethod


class TicketProvider(ABC):
    """Abstract base class for ticket/issue providers."""

    @abstractmethod
    def get_ticket_title(self, ticket_id: str) -> str:
        """
        Fetch ticket/issue title from the platform.

        Args:
            ticket_id: The ticket identifier (e.g., 'ADA-1234')

        Returns:
            The ticket title/summary as a string

        Raises:
            Exception: If the ticket cannot be found or fetched
        """
        pass

    @staticmethod
    @abstractmethod
    def get_platform_name() -> str:
        """Return the platform name for logging and error messages."""
        pass
