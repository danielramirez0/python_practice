from bs4 import BeautifulSoup
from sorting_examples.merge_sort import MergeSort
import requests



res = requests.get("https://news.ycombinator.com/")
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(article.getText().split()[0]) for article in soup.find_all(name="span", class_="score")]

mergesort = MergeSort()
mergesort.run(article_upvotes)
highest = article_upvotes[len(article_upvotes) - 1]
second_highest = article_upvotes[len(article_upvotes) - 2]

print(article_upvotes, highest, second_highest)

