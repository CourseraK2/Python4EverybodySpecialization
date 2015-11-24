import urllib
from bs4 import BeautifulSoup

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_182079.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes
sum = 0
tags = soup('span')

for tag in tags:
   sum = sum + int(tag.contents[0])

print (sum)
