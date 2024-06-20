# LinkingMap - SEO

<p align="center">
    <img src="README_SRC/main_img.png" width="500">
</p>

LinkingMap is a Python project that analyzes a webpage, extracts all links, counts the number of links by domain, and creates a visual representation of the link distribution by domain. The central node represents the scanned domain, and it is connected with lines to other domains. Self-links are colored green and labeled with "(self)".

## Project Description

This project uses the following Python libraries:
- `requests`: To fetch the webpage content.
- `BeautifulSoup` from `bs4`: To parse the HTML and extract links.
- `collections.Counter`: To count links by domain.
- `urllib.parse`: To handle and parse URLs.
- `matplotlib`: To create a visual representation.
- `networkx`: To create and manage the network graph.

## Setup Instructions

### Prerequisites

Ensure you have Python 3 and `pip` installed. You also need `virtualenv` to create an isolated environment for the project.

### Steps

1. **Clone the repository:**

```
git clone https://github.com/Liam-Nothing/LinkingMap-SEO
cd LinkingMap-SEO
```

2. **Create and activate a virtual environment:**

```
python3 -m venv venv
source venv/bin/activate
```

3. **Install the required libraries:**

```
pip install -r requirements.txt
```

## Usage Instructions

1. **Ensure your virtual environment is activated:**

```
source venv/bin/activate
```

2. **Run the script with a valid URL:**

```
python link_extractor.py https://example.com
```

Replace `https://example.com` with the URL you want to analyze. The script will fetch the webpage, extract links, count domains, and generate a bar chart saved as `domain_distribution.png`.
