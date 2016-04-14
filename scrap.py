import requests
from bs4 import BeautifulSoup

url = raw_input("Enter URL to scrap: ")
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,"html5lib")
fo = open('filename.html','w')

# attr-name > name of the tag (e.g. img)	(Required)
# attrs={'class': 'photo'} 					(Optional)

for image in soup.find_all('img',attrs={'class': 'photo'}):
	fo.write(str(image))
fo.close()

