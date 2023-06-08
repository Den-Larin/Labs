import requests

# Завдання 1:
url = input()
response = requests.get(url)
if response.status_code == 200:
    print("Сторінка доступна")
else:
    print("Сторінка недоступна")

# Завдання 2:
response = requests.get("https://en.wikipedia.org" + "/robots.txt")
if response.status_code == 200:
    print(response.text)
else:
    print("Файл robots.txt недоступний")

# Завдання 3:
response = requests.get("https://www.data.gov/")
if response.status_code == 200:
    count = response.text.count('')
    print(f"Кількість наборів даних: {count}")
else:
    print("Сторінка недоступна")
