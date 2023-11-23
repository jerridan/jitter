#!/usr/bin/env python3

import argparse
from atlassian import Jira
import git
import re

from main.config import jira_url, jira_username, jira_token


def get_jira_ticket_name(jira, ticket_number):
    issue = jira.issue(ticket_number)
    return issue["fields"]["summary"]


def generate_branch_name(ticket_number, ticket_name):
    kebob_case_name = re.sub(r"[^a-zA-Z0-9]", "-", ticket_name.lower())
    kebob_case_name = re.sub("-+", "-", kebob_case_name).strip("-")
    return f"{ticket_number}-{kebob_case_name}"


def create_git_branch(branch_name):
    repo = git.Repo.init()
    branch = repo.create_head(branch_name)
    branch.checkout()


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("ticket_number", help="Jira ticket number")
    return parser.parse_args()


def main():
    args = handle_args()
    ticket_number = args.ticket_number

    jira = Jira(url=jira_url, username=jira_username, password=jira_token)

    ticket_name = get_jira_ticket_name(jira, ticket_number)
    branch_name = generate_branch_name(ticket_number, ticket_name)

    create_git_branch(branch_name)

    print(f"Checked out to branch {branch_name}")


if __name__ == "__main__":
    main()
