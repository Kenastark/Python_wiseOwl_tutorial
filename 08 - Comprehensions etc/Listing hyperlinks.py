
import requests

response = requests.get("https://webscraper.io/test-sites/")

# test status
if response.status_code != 200:

    # print error message
    print("No URL found")
    exit()

lines = response.text.splitlines()
# print(lines)


# normal version first
# for line in lines:
#     if "<a " in line:
#         print(line.strip())


# version 2 - using list comprehension
# for line in [y.strip() for y in lines if "<a " in y]:
#     print(line)

# 









