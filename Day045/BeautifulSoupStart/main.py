from bs4 import BeautifulSoup

with open("./website.html") as file:
    htmlContents = file.read()

soup = BeautifulSoup(htmlContents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

# print(soup.a)
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# all_p_tags = soup.find_all(name="p")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

company_url = soup.select_one("p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
