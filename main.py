from bs4 import BeautifulSoup
import re
import requests
import fake_useragent

ua = fake_useragent.UserAgent()
headers = {
    "User-Agent": ua.random
}

with open('C:\\Users\\user\\Desktop\\python\\parser\\link.txt', 'r') as file:
    content = file.readlines()
    my_list = [line.strip() for line in content]
work_list  = []
# удаление дубликатов из списка
my_list = list(set(my_list))
my_list = list(filter(lambda x: x != '', my_list))
for url in my_list:
    list_url = url
    work_list.append(url)

def extract_emails(soup):  # пытается найти все email в HTML коде страницы
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    find_emails_pattern = re.findall(email_pattern, str(soup))
    unique_emails = list(set(find_emails_pattern))
    return unique_emails

    # ищет номер


def phone_numbers_extraction(soup):
    # пытается найти все номера телефонов в HTML коде странице
    # регулярное выражение для поиска номеров телефонов
    phone_pattern = r'\+?\d[\d\-\s()]{8,}\d'
    # поиск совпадений номера по переменной
    find_phones_pattern = re.findall(phone_pattern, soup)
    # удаляем лишние знаки
    deletion_of_signs = [phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '') for phone in
                         find_phones_pattern]
    # удаляем дубликаты номеров
    dell_dabl = list(set(deletion_of_signs))
    # удаляем + в начале строки
    dell_ = [number.replace('+', '') for number in dell_dabl]
    # удаляет все кроме тех которые начинаются на 7 и 8
    dell_new = [x for x in dell_ if x.startswith(('7', '8'))]
    # удаляются все которые меньше 10
    dell_new = [x for x in dell_new if len(x) > 10]
    # остаются те которые меньше или равно 11
    dell_new = [x for x in dell_new if len(x) <= 11]
    # удаляет дубли
    dell_new = list(set(dell_new))
    # возвращает список уникальных номеров телефонов
    # print(find_phones_pattern)   # проверочный принт
    return dell_new



for url in my_list:
    sent = requests.get(url, headers={"User-Agent": ua.random})
    soup = BeautifulSoup(sent.text, 'lxml')

    emails = extract_emails(soup)
    phones = phone_numbers_extraction(str(soup))

    print("URL:", url)
    print("Emails found:", emails)
    print("Phone numbers found:", phones)