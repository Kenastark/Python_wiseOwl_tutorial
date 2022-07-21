
# import sys

# append path
# sys.path.append(r"path to request module directory")

# go to website and return results
import requests

response = requests.get("https://www.bbc.co.uk")
print(response.text)