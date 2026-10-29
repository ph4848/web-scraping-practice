# Web Scraping Practice

A collection of Python web scraping projects built with **Requests** and **BeautifulSoup**. This repository includes scripts for extracting events from Python.org and collecting mobile phone product information from Technolife.

## Projects

### 1. Python.org Event Scraper

File: `src/main.py`

- Scrapes upcoming event information from Python.org.
- Extracts event titles and dates.
- Uses Requests to retrieve webpage content and BeautifulSoup to parse HTML.

### 2. Technolife Mobile Product Scraper

File: `src/app2.py`

- Scrapes mobile phone listings from Technolife.
- Extracts product titles, image URLs, and product links.
- Stores collected product information in an SQLite database named `MobileProduct.db`.

### 3. Basic HTML Website

File: `src/index.html`

A simple HTML page demonstrating headings, paragraphs, images, links, and lists.

## Project Structure

```text
web-scraping-practice/
├── README.md
├── requirements.txt
├── MobileProduct.db
└── src/
    ├── index.html
    ├── main.py
    ├── app2.py
    └── photo18243645591.jpg
```
## Requirements

- Python 3.10 or newer
- Requests
- BeautifulSoup4

## Installation

Clone the repository:

```bash
git clone https://github.com/ph4848/web-scraping-practice.git
cd web-scraping-practice
```

Create and activate a virtual environment.

On Windows:

```bash
python -m venv my_env
my_env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Python.org event scraper from the repository root:

```bash
python src/main.py
```

Run the Technolife mobile product scraper:

```bash
python src/app2.py
```

Open `src/index.html` in a web browser to view the HTML page.

## Database

The Technolife scraper creates the `MobileData` table in `MobileProduct.db` with the following fields:

| Column | Description |
|---|---|
| `id` | Automatically generated record ID |
| `title` | Product title |
| `image` | Product image URL |
| `link` | Product page URL |

Repeated scraper runs may insert duplicate products because the current script appends records without checking for existing entries.

## Disclaimer

This repository is intended for educational purposes. Please respect website terms of service, robots.txt guidance, and applicable laws when scraping websites.
