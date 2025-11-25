#!/usr/bin/env python3

import argparse
import git
import re
import os
import yaml

from .providers import create_provider
from .input_parser import parse_input


def get_config():
    config_path = os.path.expanduser("~/.jitter.yml")
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

            # Validate that at least one platform is configured
            if not config or ("jira" not in config and "linear" not in config):
                print(f"Error: No ticket systems configured in {config_path}")
                print("\nPlease add at least one platform configuration:")
                print("\nFor Jira:")
                print("jira:")
                print("  url: https://example.atlassian.net")
                print("  username: your_email@example.com")
                print("  token: your_jira_api_token")
                print("\nFor Linear:")
                print("linear:")
                print("  api_key: lin_api_xxxxxxxxxxxxx")
                print("\nSee README for detailed configuration instructions.")
                exit(1)

            return config
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
        print("\nCreate ~/.jitter.yml with at least one platform configuration.")
        print("See README for configuration instructions.")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Error reading config file at {config_path}: {e}")
        exit(1)


def generate_branch_name(ticket_number, ticket_name):
    kebob_case_name = re.sub(r"[^a-zA-Z0-9]", "-", ticket_name.lower())
    kebob_case_name = re.sub("-+", "-", kebob_case_name).strip("-")
    return f"{ticket_number}-{kebob_case_name}"


def create_git_branch(branch_name):
    current_directory = os.getcwd()
    repo = git.Repo(current_directory)

    if branch_name in repo.heads:
        branch = repo.heads[branch_name]
        print("Switching to existing branch")
    else:
        branch = repo.create_head(branch_name)
        print("Creating new branch")

    branch.checkout()


def handle_args():
    parser = argparse.ArgumentParser(
        description="Generate a git branch from a Jira or Linear ticket"
    )
    parser.add_argument(
        "ticket_input",
        metavar="ticket",
        help="Ticket identifier (e.g., ADA-1234) or full URL",
    )
    return parser.parse_args()


def main():
    # Load configuration
    config = get_config()

    # Parse user input
    args = handle_args()
    try:
        platform, ticket_id = parse_input(args.ticket_input, config)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    # Create provider and fetch ticket
    try:
        provider = create_provider(platform, config)
        ticket_title = provider.get_ticket_title(ticket_id)
    except Exception as e:
        print(f"Error fetching {platform} ticket {ticket_id}: {e}")
        exit(1)

    # Generate and create branch
    branch_name = generate_branch_name(ticket_id, ticket_title)
    create_git_branch(branch_name)

    print(f"Switched to branch: {branch_name}")


if __name__ == "__main__":
    main()
