import re
import requests
from bs4 import BeautifulSoup
with open('file.html') as file:
    r = file.read()
soup = BeautifulSoup(r, 'lxml')
print(soup.title) #1
p_tags = soup.find_all('p') #2
for tag in p_tags:
    print(tag)
count = len(p_tags) #3
print(f"Кількість тегів: {count}")
first_p = soup.find('p') #4
print(first_p.get_text())
first_h2 = soup.find('h2') #5
print(len(first_h2.get_text()))
first_a = soup.find('a') #6
print(first_a.get_text())
print(first_a.get('href')) #7
# 20
print(soup.find(href = "http:"))
# 21
parent_tags = soup.find_all('head')
for parent_tag in parent_tags:
    nested_tags = parent_tag.find_all()
    for nested_tag in nested_tags:
        print(nested_tag)
# 22
class_tags = soup.find_all(class_= "picture1")
for tag in class_tags:
    print(tag)
# 23
modify_tag = soup.find('p')
modify_tag.string = 'Element Item'
print(soup)
# 24
tag_to_append = soup.find('p')
tag_to_append.append("Item")
print(soup)
# 25
tag_to_insert = soup.find('a')
tag_to_insert.insert(3, "Item")
print(soup)
# 26
tag_to_insert_before = soup.find('p')
tag = soup.new_tag('i')
tag.string = "HTML"
tag_to_insert_before.string.insert_before(tag)
print(soup)
# 27
tag_to_insert_after = soup.find('p')
tag = soup.new_tag('i')
tag.string = "HTML"
tag_to_insert_after.string.insert_after(tag)
print(soup)
# 28
tag_to_clear = soup.find('a')
tag_to_clear.clear()
print(soup)
# 29
tag_to_extract = soup.find('p')
tag = soup.find('i')
tag_i = soup.i.extract()
print(soup)
# 30
tag_to_clear = soup.find('a')
tag_to_clear.decompose()
print(soup)
# 31
tag_to_replace = soup.find('p')
new_tag = soup.new_tag('k')
new_tag.string = 'Office'
k_tag = tag_to_replace.replace_with(new_tag)
print(soup)
# 32
tag_to_wrap = soup.find('p')
soup.p.string.wrap(soup.new_tag('i'))
soup.p.wrap(soup.new_tag('div'))
print(soup)
# 33
tag_to_rpl = soup.find('p')
tag_to_rpl.i.unwrap()
print(soup)

