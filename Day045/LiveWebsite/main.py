from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

all_titles = soup.select(".titleline")

art_titles = [title.find(name="a").getText() for title in all_titles]
print(art_titles)

art_links = [title.find(name="a").get("href") for title in all_titles]
print(art_links)

all_scores = soup.select(".score")
scores = [int(score.getText().split(" ")[0]) for score in all_scores]
print(scores)

max_index = scores.index(max(scores))
print(art_titles[max_index])
print(art_links[max_index])
print(scores[max_index])
