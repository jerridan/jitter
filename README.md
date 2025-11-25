# Jitter

A tool that generates a git branch given a Jira or Linear ticket.

## Pre-requisites

- Python 3.8 or newer. You can check your Python version using `python --version`. Consider using pyenv to manage and
  install different python versions.
- Poetry for Python package and environment management. Follow the directions [here](https://python-poetry.org/docs/)
  for installation instructions.

## Installation Steps

1. Clone the Github repository

    ```bash
    git clone https://github.com/jerridan/jitter
    cd jitter
    ```

2. Install the dependencies in a virtual environment using Poetry

    ```bash
    make init
    ```

3. Package the script into an executable using Pyinstaller

    ```bash
    make build
    ```

4. Add the resulting executable (located in `dist` folder) to your PATH

    ```bash
    echo 'export PATH="$PATH:/absolute/path/to/jitter/dist"' >> ~/.zshrc # or ~/.bashrc if you use bash
    source ~/.zshrc
    ```

## Configuration

To use the Jitter script, you need to set up a YAML configuration file named `.jitter.yml` in your home directory.
You can configure Jira, Linear, or both platforms.

Follow these steps:

### Step 1: Create .jitter.yml file in your home directory

You can do this by running the following command in your terminal:

`touch ~/.jitter.yml`

### Step 2: Add platform configuration(s)

Open `~/.jitter.yml` in a text editor and add configuration for at least one platform.

#### For Jira Only:

```yaml
jira:
  url: https://example.atlassian.net
  username: your_email@example.com
  token: your_jira_api_token
```

**Obtaining your Jira API token:**
Generate a new API token from your [Atlassian account settings](https://id.atlassian.com/manage-profile/security),
under Security > API tokens.

#### For Linear Only:

```yaml
linear:
  api_key: lin_api_xxxxxxxxxxxxx
```

**Obtaining your Linear API key:**
1. Visit https://linear.app/settings/api
2. Create a new Personal API Key
3. Give it a descriptive name (e.g., "Jitter CLI")
4. Copy the key to your configuration file

#### For Both Platforms:

```yaml
jira:
  url: https://example.atlassian.net
  username: your_email@example.com
  token: your_jira_api_token

linear:
  api_key: lin_api_xxxxxxxxxxxxx
```

**Note:** Treat your API tokens and keys like passwords and keep them secret. They link to your accounts until you revoke them.

## Usage

After installing the Jitter project, from any directory just run:

`jitter [ticket identifier or URL]`

This will create a new branch using the ticket summary/title.

### Usage Examples

#### Using Ticket IDs

If you have **only one platform configured**, you can use ticket IDs directly:

```bash
# With only Jira configured
jitter ADA-1234

# With only Linear configured
jitter ADA-1234
```

If you have **both platforms configured**, you must use the full URL to specify which platform:

#### Using URLs (Works with any configuration)

```bash
# Jira ticket by URL
jitter https://example.atlassian.net/browse/ADA-1234

# Linear issue by URL
jitter https://linear.app/ada/issue/ADA-1234/issue-title
```

### Branch Naming

The tool automatically generates a branch name in kebab-case format:

**Format:** `{TICKET-ID}-{kebab-case-title}`

**Example:** If your ticket ID is `ADA-1234` and the title is `Add a new feature`, the branch name will be `ADA-1234-add-a-new-feature`.

Happy Coding!
