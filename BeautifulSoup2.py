import re
import requests
from bs4 import BeautifulSoup

url = 'https://python.org/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

# 8
li_tags = soup.find_all('li')
for li in li_tags:
    link = li.find('a')
    href = link.get('href')
    print(href)
# 9
h2_tags = soup.find_all('h2')
for i in range(4):
    if i < len(h2_tags):
        print(h2_tags[i])
# 10
a_tags = soup.find_all('a')
for i in range(10):
    if i < len(a_tags):
        print(a_tags[i].get('href'))
# 11
h_tags = soup.find_all(['h1', 'h2', 'h3'])
for i in h_tags:
    print(i)
# 12
print(soup.get_text())
# 13
tags = soup.find_all()
for tag in tags:
    print(tag.name)
# 14
html_tag = soup.find('html')
if html_tag:
    nested_tags = html_tag.find_all()
    for tag in nested_tags:
        print(tag.name)
#15
body_tag = soup.find('body')
body_tag_child = [tag.name for tag in body_tag.descendants if tag.name is not None]
print(body_tag_child)
#16
print(soup.title)
print(soup.title.get_text())
print(soup.title.parent)
#17
li_tags = soup.find_all('li')
for tag in li_tags:
    print(tag)
#18
text = soup.find_all(string = re.compile('Python'))
for txt in text:
    print(txt)
#19
print(soup.select('#my-id'))

