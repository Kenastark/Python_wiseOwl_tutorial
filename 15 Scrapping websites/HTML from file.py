
# get HTML from a file
with open("/Users/ikenna/Documents/GitHub/Python/15 Scrapping websites/Files needed/wyndham.htm") as wyndham_file:
    # store the response
    html_text = wyndham_file.read()

print(html_text)