# DAY 22: 30 Days of python programming

#1
import requests
from bs4 import BeautifulSoup
import json

URL = "http://www.bu.edu/president/boston-university-facts-stats/"

# Send request
response = requests.get(URL)
print(response.text)
