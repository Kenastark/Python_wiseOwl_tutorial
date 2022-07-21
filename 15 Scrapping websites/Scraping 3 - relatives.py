
# get HTML from a file
with open("/Users/ikenna/Documents/GitHub/Python/15 Scrapping websites/Files needed/wyndham.htm") as wyndham_file:

    # store the response
    html_file = wyndham_file.read()

from bs4 import BeautifulSoup

# parse the HTML
soup = BeautifulSoup(html_file,"html.parser")

# refer to the first div tag
div = soup.div

# # look at immediate children Only shows the child one-level down
# for child in div.contedents:
#     print(child)

# look at all descendants. it trickles down to the deeper sub layer
for child in div.descendants:
    print(child)







