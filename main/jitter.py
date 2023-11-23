#!/usr/bin/env python3

import argparse
from atlassian import Jira
import git
import re
import os
import yaml


def get_config():
    config_path = os.path.expanduser("~/.jitter.yml")
    try:
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Error reading config file at {config_path}: {e}")
        exit(1)


def get_jira_ticket_name(jira, ticket_number):
    issue = jira.issue(ticket_number)
    return issue["fields"]["summary"]


def generate_branch_name(ticket_number, ticket_name):
    kebob_case_name = re.sub(r"[^a-zA-Z0-9]", "-", ticket_name.lower())
    kebob_case_name = re.sub("-+", "-", kebob_case_name).strip("-")
    return f"{ticket_number}-{kebob_case_name}"


def create_git_branch(branch_name):
    current_directory = os.getcwd()
    repo = git.Repo(current_directory)

    if branch_name in repo.heads:
        print(f"Branch {branch_name} already exists")
        return

    branch = repo.create_head(branch_name)
    branch.checkout()


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("ticket_number", help="Jira ticket number")
    return parser.parse_args()


def main():
    config = get_config()

    jira_url = config["jira"]["url"]
    jira_username = config["jira"]["username"]
    jira_token = config["jira"]["token"]

    args = handle_args()
    ticket_number = args.ticket_number

    jira = Jira(url=jira_url, username=jira_username, password=jira_token)

    ticket_name = get_jira_ticket_name(jira, ticket_number)
    branch_name = generate_branch_name(ticket_number, ticket_name)

    create_git_branch(branch_name)

    print(f"Checked out to branch {branch_name}")


if __name__ == "__main__":
    main()
