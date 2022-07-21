
# get HTML from a file
with open("/Users/ikenna/Documents/GitHub/Python/15 Scrapping websites/Files needed/wyndham.htm") as wyndham_file:

    # store the response
    html_text = wyndham_file.read()

    from bs4 import BeautifulSoup

    # parse the HTML
    soup = BeautifulSoup(html_text, "html.parser")

# show the visible text of the first book
print(soup.td.a.string.strip())

# print out all the visible books
link_text = soup.table.stripped_strings
for t in link_text:
    print(t)

