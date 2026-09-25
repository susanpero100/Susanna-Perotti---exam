## Campaign Validator 
is a small Python command-line application for checking advertising campaign data. It normalizes a campaign name, calculates a click-through-rate percentage, counts campaign tags, and verifies that the local campaign access token is configured correctly.
## Setup Use uv to install the project dependencies:
uv sync

## Configuration
Create a .env file in the project folder and add the access token provided by the instructor:
CAMPAIGN_ACCESS_TOKEN=your_token_here
The .env file is local and should not be committed.
Run
Run the application with:
uv run campaign-validator

## Quality checks
Run the quality checks with:
uv run ruff format --check .
uv run ruff check .
uv run mypy .
uv run pytest


