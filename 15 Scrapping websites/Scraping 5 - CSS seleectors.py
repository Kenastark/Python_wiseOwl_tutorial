
# get HTML file
with open("/Users/ikenna/Documents/GitHub/Python/15 Scrapping websites/Files needed/wyndham.htm") as wyndham_file:

    # store the response
    html_file = wyndham_file.read()
# print(html_file)
from bs4 import BeautifulSoup

# # parse the HTML
soup = BeautifulSoup(html_file, "html.parser")

# searching by tag
# for header in soup.select("th"):
#     print(header)

# searching by class
# for element in soup.select(".link"):
#     print(element.string.strip())

# searching by id 
top_div = soup.select_one("#table-box")
print(top_div)







