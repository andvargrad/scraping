import re
import requests
import csv

numbers = []
numbers1 = []
with open('urls.csv') as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader]

for url in urls:
    response = requests.get(url)
    emails = set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text))

    phones = set(re.findall(r'(\+?\d[\d\-\s\(\)]{8,}\d)', response.text))
    final_list = [phone.translate(str.maketrans('', '', ',()- ')) for phone in phones]

for i in final_list:
    len_list = len(i)
    if len_list == 11 or len_list == 12:
        numbers.append(i)

for j in numbers:
    if j[0] == "+" or j[0] == "7" or j[0] == "8":
        numbers1.append(j)


with open("numbers.txt", 'a') as f:
    for number in numbers1:
        f.write(number + "\n")
    f.close()

with open("email.txt", 'a') as f:
    for email in emails:
        f.write(email + "\n")
    f.close()


print(f'Телефоны: - {set(numbers1)}')
print(f'Почта: - {emails}')


