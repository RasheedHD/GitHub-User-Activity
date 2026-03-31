# GitHub User Activity

A simple command-line Python app that fetches and displays a GitHub user's recent public activity using the GitHub Events API.

## Features

- Fetches recent public activity for any GitHub username
- Handles multiple event types, including:
  - Push events
  - Repository, branch, and tag creation
  - Stars
  - Issue activity
- Gracefully handles invalid users and URL errors
- Uses only Python standard library modules

## Technologies Used

- Python
- `urllib.request`
- `json`

## How It Works

The program:

1. Prompts the user to enter a GitHub username
2. Sends a request to the GitHub Events API
3. Parses the returned JSON data
4. Loops through the activity events
5. Prints a readable summary of each supported event

## Example Output

    > octocat
    - Pushed to octocat/Hello-World
    - Starred octocat/Spoon-Knife
    - Created branch in octocat/test-repo
    - Opened a new issue in octocat/Hello-World

## Installation

Clone the repository:

    git clone https://github.com/your-username/github-user-activity.git
    cd github-user-activity

## Usage

Run the script with Python:

    python main.py

Then enter a GitHub username when prompted:

    > torvalds

## Project Structure

    .
    ├── main.py
    └── README.md

## Supported Event Types

This project currently supports:

- `PushEvent`
- `CreateEvent`
- `WatchEvent`
- `IssuesEvent`

## Error Handling

The program handles:

- `HTTPError` for invalid users or failed HTTP requests
- `URLError` for connection or URL-related problems

## Limitations

- Only public activity is shown
- Only selected GitHub event types are handled
- Output depends on the activity currently available from the GitHub API

## Possible Improvements

- Support more GitHub event types
- Improve output formatting
- Add commit counts for push events when available
- Convert the script into a reusable CLI tool with command-line arguments
- Add tests

## API Used

This project uses the GitHub Events API:

    https://api.github.com/users/<username>/events

## Learning Goals

This project is a good exercise for practicing:

- Working with APIs
- Making HTTP requests in Python
- Parsing JSON data
- Handling exceptions
- Writing simple CLI applications

## License

This project is for learning and practice purposes.

Project taken from: https://roadmap.sh/projects/github-user-activity