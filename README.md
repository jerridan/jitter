# Jitter

A tool that generates a git branch given a jira ticket number.

## Pre-requisites

- Python 3.8 or newer. You can check your Python version using `python --version`. Consider using pyenv to manage and install different python versions.
- Poetry for Python package and environment management. Follow the directions [here](https://python-poetry.org/docs/) for installation instructions.

## Installation Steps

1. Clone the Github repository

    ```bash
    git clone https://github.com/jerridan/jitter
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
    echo 'export PATH="$PATH:/path/to/jitter/dist"' >> ~/.zshrc # or ~/.bashrc if you use bash
    source ~/.zshrc
    ```

Replace `/path/to/jitter/dist` with the absolute path to the `dist` directory that was created by Pyinstaller.

## Usage

After installing the Jitter project, from any directory just run `jitter [ticket number]` to create a new branch with the ticket information. Replace `[ticket number]` with your specific Jira ticket number.

Happy Coding!
