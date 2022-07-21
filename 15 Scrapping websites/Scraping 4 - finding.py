
# get HTML file
with open("/Users/ikenna/Documents/GitHub/Python/15 Scrapping websites/Files needed/wyndham.htm") as wyndham_file:

    # store the response
    html_file = wyndham_file.read()
# print(html_file)
from bs4 import BeautifulSoup

# # parse the HTML
soup = BeautifulSoup(html_file, "html.parser")
# # print(soup)
# # finding elements by tag
# links = soup.find_all("a")
# for link in links:
    
#     url = link.get("href")
#     print(str(url).strip())


# finding element by attributes

# Get element with given ID
# element = soup.find_all(id="table-box")
# for el in element:
#     print(el.name)

# # show elements with src attributes
# srcs = soup.find_all(src=True)
# for src in srcs:
#     print(src)

# finding elements by class
# classy_links = soup.find_all(class_="link")

# for lk in classy_links:
#     print(lk.string.strip())


# non-recursive finds

# list all the div tags
tags = soup.find_all("div", recursive=True)
for tag in tags:
    print(tag)


