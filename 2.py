import requests
from bs4 import BeautifulSoup

# Время выполнения кода - пару минут
#Советую расскоментировать все print, так выполнение программы будет более наглядным


site = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

response = requests.get(site)

request_flag = 0; # Проверка первого подключения
flag_break = 0;
list_names = [] # Список имен животных

#Цикл выполняется до тех пор, пока не будет найдено первое слово на лат.языке
while flag_break != 1:

    # print(site)
    flag_flag = 0;
    soup = BeautifulSoup(response.text, 'html.parser')

    for i in range(len(soup.find("div", class_="mw-category mw-category-columns").text.split("\n"))):
        #Получаем "доступ" к списку животных
        if i != 0 and soup.find("div", class_="mw-category mw-category-columns").text.split("\n")[i] != "Helobdella nununununojensis"  :

            # Проверка на "Helobdella nununununojensis" необходима, т.к в вики есть небольшая ошибка, в результате который среди имен
            # животных на русском языке затесалось слово на лат.языке

            if soup.find("div", class_="mw-category mw-category-columns").text.split("\n")[i][0] == "A":
                flag_break = 1

                # print("\n\nФенита ля Комедия!")
                # Данное условие необходимо для того, чтобы проверить не встретилось ли животное, имя которого написано на лат.языке,
                # в случае нахождение такого программа прекращает свою работу!

                break

            list_names.append(soup.find("div", class_="mw-category mw-category-columns").text.split("\n")[i])
            # print(soup.find("div", class_="mw-category mw-category-columns").text.split("\n")[i], end = " ")
                # Выводим имена животных, которые встретились на странице

    # print()

    # Ищем ссылку на Следующую страницу
    for a in soup.find("div", id="mw-pages").find_all('a', href=True):
        if request_flag == 0:
            site = "https://ru.wikipedia.org" + a['href']
            request_flag = 1
            # Если мы находимся на первой странице вики, то ссылка на следующую страницу будет первой, поэтому мы
            # сразу же выходим из цикла
            break;
        else:
            flag_flag += 1
            if flag_flag == 2:
                site = "https://ru.wikipedia.org" + a['href']
                # Если мы находимся не на первой странице википедии, то ссылка на следующую страницу будет второй
                break;


    response = requests.get(site)

animals = dict()
for i in range(len(list_names)):
    if list_names[i][0] in animals:
        value = animals.get(list_names[i][0]) + 1
        animals[list_names[i][0]] = value
        # print("Буква '", list_names[i][0], "' встретилась уже в ", animals[list_names[i][0]], " раз!")
    else:
        # print("Вставили буковку '", list_names[i][0], "' первый раз в словарь!")
        animals[list_names[i][0]] = 1

animals = sorted(animals.items())

for key in animals:
    print(key)




