from bs4 import BeautifulSoup
from sorting_examples.merge_sort import MergeSort
import requests

def get_largest_index(arr) -> int:
    i = 0
    largest = arr[i]
    largest_index =0

    for vote in arr:
        if vote > largest:
            largest_index = i
        i += 1
    return largest_index

def get_largest_builtin(arr:list) -> int:
    largest = max(arr)
    largest_i = arr.index(largest)
    return largest_i

def get_second_largest(arr:list) -> int:
    buffer = arr[:]
    m = MergeSort()
    m.sort(buffer)
    target = buffer[len(buffer) - 2]
    solution = arr.index(target)
    return solution

# mergesort = MergeSort()
# mergesort.run(article_upvotes)
# highest = article_upvotes[len(article_upvotes) - 1]
# second_highest = article_upvotes[len(article_upvotes) - 2]

res = requests.get("https://news.ycombinator.com/")
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(article.getText().split()[0]) for article in soup.find_all(name="span", class_="score")]

print(article_upvotes)
print(get_largest_index(article_upvotes))
print(get_largest_builtin(article_upvotes))
print(get_second_largest(article_upvotes))