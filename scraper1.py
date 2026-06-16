import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

titles, prices, ratings = [], [], []

for page in range(1, 6):
    url = base_url.format(page)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print(f"Error on page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        titles.append(book.h3.a["title"])
        prices.append(book.find("p", class_="price_color").text)
        ratings.append(book.find("p")["class"][1])

    time.sleep(1)

df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings
})

# Clean price
df["Price"] = df["Price"].str.replace(r'[^\d.]', '', regex=True).astype(float)

df.to_csv("advanced_books.csv", index=False)

print("Advanced scraping completed!")