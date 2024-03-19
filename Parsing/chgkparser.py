from bs4 import BeautifulSoup
import requests
url = 'https://db.chgk.info/tour/disharm5_u'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')

paragraph = soup.find_all(class_='question')

file = open("parsing.txt", "a")

for item in paragraph:
    paragraph_text = item.text
    file.write(paragraph_text)

file.close()