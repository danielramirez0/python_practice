import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(URL)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

elements = soup.find_all(name="h3", class_="title")
elements.reverse() # or use elements[::-1] slice operator
titles = [element.getText() for element in elements]

with open("movies.txt", mode="w") as file:
    for movie in titles:
        file.write(f"{movie}\n")

