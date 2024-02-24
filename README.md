# NBA Player Stats Scraper

This Python script scrapes NBA player statistics from the official NBA website and organizes the data into separate CSV files based on different categories. It utilizes the `requests` library for making HTTP requests, `BeautifulSoup` for web scraping, and writes the data to CSV files.

## Features

- **Web Scraping:** Utilizes BeautifulSoup to extract player names and points from the NBA website.
- **CSV Organization:** Organizes player data into separate CSV files based on different statistical categories.

## Tech Stack

- **requests:** Python library for making HTTP requests.
- **BeautifulSoup:** Python library for web scraping.

## Usage

1. **Run the Script:**
   - Execute the script using Python: `python main.py`.

2. **Check CSV Files:**
   - Find separate CSV files for each statistical category, organized by player names and points.

## Code Snippet

```python
import csv
import requests
from bs4 import BeautifulSoup
from secret import USER_AGENT, ACCEPT, ACCEPT_ENCODING, ACCEPT_LANGUAGE, REQUEST_LINE
```

## Notes
- Ensure you have the necessary dependencies installed before running the script.

## Licence
- This script is licensed under the MIT License - see the LICENSE file for details.
