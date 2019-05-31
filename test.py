from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.google.com'

soup = BeautifulSoup(urlopen('google.com').read(), features="lxml")
print(soup.title.string)