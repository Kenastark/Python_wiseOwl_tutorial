
# get HTML from a file
with open("/Users/ikenna/Documents/GitHub/Python/15 Scrapping websites/Files needed/wyndham.htm") as wyndham_file:

    # store the response
    html_text = wyndham_file.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_text, "html.parser")

print(soup.prettify())