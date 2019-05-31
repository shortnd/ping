from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.google.com'

soup = BeautifulSoup(urlopen('http://cms2.revize.com/').read(), features="lxml")
print(soup.title.string)