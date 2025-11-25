from main.providers.base import TicketProvider
from main.providers.jira import JiraProvider
from main.providers.linear import LinearProvider


def create_provider(platform: str, config: dict) -> TicketProvider:
    """
    Factory function to create the appropriate ticket provider.

    Args:
        platform: The platform name ('jira' or 'linear')
        config: The full configuration dictionary

    Returns:
        An instance of the appropriate TicketProvider subclass

    Raises:
        ValueError: If the platform is not supported or not configured
    """
    if platform == "jira":
        if "jira" not in config:
            raise ValueError("Jira is not configured in ~/.jitter.yml")
        return JiraProvider(config["jira"])
    elif platform == "linear":
        if "linear" not in config:
            raise ValueError("Linear is not configured in ~/.jitter.yml")
        return LinearProvider(config["linear"])
    else:
        raise ValueError(f"Unsupported platform: {platform}")


__all__ = ["TicketProvider", "JiraProvider", "LinearProvider", "create_provider"]
