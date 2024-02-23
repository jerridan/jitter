# Jitter

A tool that generates a git branch given a jira ticket number.

## Pre-requisites

- Python 3.8 or newer. You can check your Python version using `python --version`. Consider using pyenv to manage and
  install different python versions.
- Poetry for Python package and environment management. Follow the directions [here](https://python-poetry.org/docs/)
  for installation instructions.

## Installation Steps

### Using Docker

1. Clone the Github repository and navigate to the project directory

    ```bash
    git clone https://github.com/jerridan/jitter
    cd jitter
    ```

2. Build the Docker image

    ```bash
    docker build -t jitter .
    ```   

3. Create a temporary Docker container

    ```bash
    docker create --name temp-container jitter
    ```

4. Copy the executable from the container to your local directory

    ```bash
    docker cp temp-container:/usr/src/app/dist/jitter ./path/to/local/directory
    ```

5. Remove the temporary container

   ```bash
   docker rm temp-container
   ```
   
6. Add the jitter executable to your PATH

    ```bash
    echo 'export PATH="$PATH:/absolute/path/to/jitter"' >> ~/.zshrc # or ~/.bashrc if you use bash
    source ~/.zshrc
    ```

### Locally

1. Clone the Github repository

    ```bash
    git clone https://github.com/jerridan/jitter
    cd jitter
    ```

2. Install the dependencies using Poetry

    ```bash
    poetry install
    ```

3. Package the script into an executable using Pyinstaller

   Use Pyinstaller to package the script:

    ```bash
    poetry run pyinstaller --onefile main/jitter.py
    ```

4. Add the resulting executable (located in `dist` folder) to your PATH

    ```bash
    echo 'export PATH="$PATH:/absolute/path/to/jitter/dist"' >> ~/.zshrc # or ~/.bashrc if you use bash
    source ~/.zshrc
    ```

## Configuration

To use the Jitter Python script, you need to set up a YAML configuration file named .jitter.yml in your home directory.
It requires your Jira configuration details including username and API token.

Follow these steps:

### Step 1: Obtain your Jira API token.

You can generate a new API token from
your [Atlassian account settings](https://id.atlassian.com/manage-profile/security), under Security > API tokens.

### Step 2: - Create .jitter.yml file in your home directory.

You can do this by running the following command in your terminal:

`touch ~/.jitter.yml`

### Step 3: - Open ~/.jitter.yml in a text editor and add your Jira configuration inside it.

The file should have the following format:

```yaml
jira:
  url: your_jira_url # ex. https://example.atlassian.net
  username: your_jira_username
  token: your_jira_token
```

Replace your_jira_url, your_jira_username, and your_jira_token with your actual Jira details.

Note: Treat your API tokens like passwords and keep them secret. API tokens link to your Atlassian account until you
revoke them.

## Usage

After installing the Jitter project, from any directory just run:

`jitter [ticket number]`

This will create a new branch using the summary. Replace `[ticket number]` with your specific Jira ticket number.

For example, if your Jira ticket number is `ADA-1234`, run: `jitter ADA-1234`

If the ticket summary is `Add a new feature`, the branch name will be `ADA-1234-add-a-new-feature`.

Happy Coding!
