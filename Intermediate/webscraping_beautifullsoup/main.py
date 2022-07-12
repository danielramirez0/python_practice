from bs4 import BeautifulSoup
# import lxml # (parser used for some websites which don't like html parser)

with open("website.html") as site:
    contents = site.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

nested_selector = soup.select_one(selector="p a") # css selector code
name = soup.select_one(selector="#name")
seleted_classes = soup.select(selector=".heading")

print(nested_selector,name,seleted_classes)
