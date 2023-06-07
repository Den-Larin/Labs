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
