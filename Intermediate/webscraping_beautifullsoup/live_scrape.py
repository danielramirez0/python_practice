from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/")
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(article.getText().split()[0]) for article in soup.find_all(name="span", class_="score")]

highest = article_upvotes[0]
for votes in article_upvotes:
    if votes > highest:
        highest = votes

# max = float("-inf")
for vote in article_upvotes:
    pass

print(highest) 
