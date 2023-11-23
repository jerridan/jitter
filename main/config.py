import os
from dotenv import load_dotenv

load_dotenv()

jira_url = os.environ.get("JIRA_URL")
jira_username = os.environ.get("JIRA_USERNAME")
jira_token = os.environ.get("JIRA_TOKEN")
