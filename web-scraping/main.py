import requests
from bs4 import BeautifulSoup
# import lxml (another parser)

# Just messing around with beautiful soup functions:
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
#
# anchors = soup.find_all(name="a")
# print(anchors)
#
# for anchor in anchors:
#     print(anchor.get("href"))
#
# heading = soup.find(id="name")
# print(heading)
#
# heading = soup.find(class_="heading")
# print(heading.getText())
#
# company = soup.select_one(selector="p a")  # css selector
# print(company)
#
# headings = soup.select(selector=".heading")  # css selector
# print(headings)


# Get most viewed article
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
news = soup.find_all("tr", class_="athing")
scores = soup.find_all("span", class_="score")

texts = []
links = []
for article in news:
    row = article.select_one("span a")
    texts.append(row.getText())
    links.append(row.get("href"))

votes = [int(score.getText().split(" ")[0]) for score in scores]

most_voted = votes.index(max(votes))
print(texts[most_voted], links[most_voted])


# Top 100 movies to watch:
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

movies = []
titles = soup.find_all("h3", class_="title")
for title in reversed(titles):
    try:
        movies.append(title.getText().split(")")[1])
    except IndexError:
        movies.append(title.getText().split(":")[1])

with open("titles.txt", mode="w") as file:
    for index, movie in enumerate(movies):
        file.write(f"{index + 1})" + movie + "\n")
