import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urljoin

url = "https://www.technolife.com/category/mobile/mobile-phone"
DB_NAME = "MobileProduct.db"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Correct product-card selector
cards = soup.select("article > section")
print("Cards found:", len(cards))

conn = sqlite3.connect(DB_NAME)

try:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MobileData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            image TEXT,
            link TEXT
        )
    """)

    products = []

    for card in cards:
        # Find the product link
        product_link = card.select_one('a[href^="/product-"]')
        if not product_link:
            continue

        link = urljoin(url, product_link["href"])

        # Find the product image
        image_tag = card.select_one("img")
        if not image_tag:
            continue

        # Get title from the image's title attribute
        title = (
            image_tag.get("title")
            or product_link.get_text(" ", strip=True)
        ).strip()

        image = (
            image_tag.get("src")
            or image_tag.get("data-src")
            or image_tag.get("data-lazy-src")
        )

        if not title or not image:
            continue

        img_url = urljoin(url, image)

        products.append((title, img_url, link))

    cursor.executemany("""
        INSERT INTO MobileData (title, image, link)
        VALUES (?, ?, ?)
    """, products)

    conn.commit()
    print(f"\nSaved {len(products)} products.")

except Exception:
    conn.rollback()
    raise

finally:
    conn.close()
