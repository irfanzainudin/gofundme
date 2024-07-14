from bs4 import BeautifulSoup
import requests

url = "https://www.gofundme.com/"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

with open("test.html", 'w') as write_to_file:
    write_to_file.write(soup.prettify())