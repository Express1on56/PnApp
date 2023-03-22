from bs4 import BeautifulSoup
import requests

# отправляем GET-запрос на страницу
url = 'http://ms560024:155941@172.31.113.137:8080/MVO/do?action=AttachPeopleTotalPage'
response = requests.get(url)

# парсим HTML-страницу с помощью BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# ищем все ссылки на странице
links = soup.find_all('a', href=True)

# проходим по каждой ссылке и ищем нужный текст в URL
for link in links:
    if 'Division=All&Section=All&FAP=All' in link['href']:
# ссылка содержит нужный текст
        csv_link = 'http://ms560024:155941@172.31.113.137:8080/MVO/' + link['href']
        print(csv_link)
        break
# если ссылка найдена, скачиваем файл

if csv_link:
# отправляем GET-запрос на сервер для получения файла
    response = requests.get(csv_link)

# сохраняем содержимое файла в локальный файл
    with open('AttachPeopleTotal.csv', 'wb') as f:
        f.write(response.content)

    print('Файл с прикрепленным населением успешно скачан')

else:
    print('Ссылка не найдена')