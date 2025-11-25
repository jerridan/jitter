import re


# URL patterns for extracting ticket IDs
JIRA_URL_PATTERN = r"atlassian\.net/browse/([A-Z]+-\d+)"
LINEAR_URL_PATTERN = r"linear\.app/[^/]+/issue/([A-Z]+-[A-Za-z0-9]+)"


def extract_from_url(url: str) -> tuple[str, str] | None:
    """
    Extract platform and ticket ID from a URL.

    Args:
        url: The URL to parse

    Returns:
        A tuple of (platform, ticket_id) or None if URL doesn't match known patterns

    Examples:
        >>> extract_from_url("https://example.atlassian.net/browse/ADA-1234")
        ("jira", "ADA-1234")
        >>> extract_from_url("https://linear.app/ada/issue/ADA-1234/title")
        ("linear", "ADA-1234")
    """
    # Check for Jira URL
    jira_match = re.search(JIRA_URL_PATTERN, url)
    if jira_match:
        return ("jira", jira_match.group(1))

    # Check for Linear URL
    linear_match = re.search(LINEAR_URL_PATTERN, url)
    if linear_match:
        return ("linear", linear_match.group(1))

    return None


def detect_platform_from_id(ticket_id: str, config: dict) -> str | None:
    """
    Detect which platform a ticket ID belongs to based on configuration.

    Args:
        ticket_id: The ticket identifier
        config: The configuration dictionary

    Returns:
        The platform name ("jira" or "linear") or None if ambiguous

    Raises:
        ValueError: If both platforms are configured (ambiguous)
                   or if no platforms are configured
    """
    has_jira = "jira" in config
    has_linear = "linear" in config

    if not has_jira and not has_linear:
        raise ValueError(
            "No ticket systems configured. Please add 'jira' or 'linear' "
            "section to ~/.jitter.yml"
        )

    if has_jira and has_linear:
        raise ValueError(
            f"Ambiguous ticket ID '{ticket_id}'. Both Jira and Linear are configured.\n"
            "Please provide the full URL to specify which platform to use:\n"
            "  - Jira: https://example.atlassian.net/browse/{ticket_id}\n"
            "  - Linear: https://linear.app/workspace/issue/{ticket_id}/title"
        )

    if has_jira:
        return "jira"
    else:
        return "linear"


def parse_input(user_input: str, config: dict) -> tuple[str, str]:
    """
    Parse user input to extract platform and ticket ID.

    Args:
        user_input: The user-provided input (URL or ticket ID)
        config: The configuration dictionary

    Returns:
        A tuple of (platform, ticket_id)

    Raises:
        ValueError: If the input cannot be parsed or is ambiguous

    Examples:
        >>> parse_input("ADA-1234", {"jira": {...}})
        ("jira", "ADA-1234")
        >>> parse_input("https://linear.app/ada/issue/ADA-1234/title", config)
        ("linear", "ADA-1234")
    """
    # Check if input looks like a URL
    if user_input.startswith(("http://", "https://")):
        result = extract_from_url(user_input)
        if result is None:
            raise ValueError(
                f"Could not parse URL: {user_input}\n"
                "Supported formats:\n"
                "  - Jira: https://example.atlassian.net/browse/TICKET-123\n"
                "  - Linear: https://linear.app/workspace/issue/TICKET-123/title"
            )
        return result

    # Treat as ticket ID
    ticket_id = user_input.strip()
    platform = detect_platform_from_id(ticket_id, config)
    return (platform, ticket_id)
