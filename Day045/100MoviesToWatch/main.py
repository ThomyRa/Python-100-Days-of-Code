import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

all_titles = soup.select(" h3.title")
movies = [title.getText() for title in all_titles]
print(movies[::-1])

with open("./MovieList.txt", "w", encoding="utf8") as file:
    for movie in movies[::-1]:
        file.writelines(f"{movie}\n")




