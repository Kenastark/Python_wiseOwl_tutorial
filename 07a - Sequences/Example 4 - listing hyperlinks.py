
import requests

response = requests.get("https://webscraper.io/test-sites/")

# test status
if response.status_code != 200:

    # print error message
    print("No URL found")
    exit()

lines = response.text.splitlines()

# loop over the lines printing them out
for line in lines:
   
   # trim this line // trim a line means removing any spaces before and after it
   trimmed_line = line.strip()
   
   # is this a hyperlink?
   if "<a " in trimmed_line:
       print(trimmed_line)
       



