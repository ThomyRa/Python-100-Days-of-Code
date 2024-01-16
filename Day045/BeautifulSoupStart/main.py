from bs4 import BeautifulSoup

with open("./website.html") as file:
    htmlContents = file.read()

soup = BeautifulSoup(htmlContents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

print(soup.a)
print(soup.p)


