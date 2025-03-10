import requests
from bs4 import BeautifulSoup

# Function to scrape book details from a single page
def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Availability: {availability}")
        print("-" * 40)

# Base URL for pagination
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Scrape all pages (assumes there are 50 pages)
for page in range(1, 51):
    print(f"\nScraping Page {page}...\n")
    scrape_books(base_url.format(page))
