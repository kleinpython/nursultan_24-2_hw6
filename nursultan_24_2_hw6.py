import re

with open('MOCK_DATA.txt', 'r') as file:
    data = file.read()

while True:
    option = input('Выберит опцию:\n'
                   '1 - Имя и Фамилия\n'
                   '2 - Почта\n'
                   '3 - Название файла\n'
                   '4 - Цвета\n'
                   '5 - Выход\n')
    option = int(option)
    if option == 5:
        break

    if option == 1:
        with open('full_name.txt', 'w') as file:
            names = re.findall(r'\b[A-Z][A-Za-z\-]+\s[a-zA-Z\'\- ]+\b', data)
            for name in names:
                file.write(name + '\n')

    if option == 2:
        with open('email.txt', 'w') as file:
            mails = re.findall(r'\b[\w\-]+@[\w\.\-]+\b', data)
            for mail in mails:
                file.write(mail + '\n')

    if option == 3:
        with open('file_name.txt', 'w') as file:
            files = re.findall(r'\s[\w]+\.[\w]+\b', data)
            for file_name in files:
                file.write(file_name[1:] + '\n')

    if option == 4:
        with open('color.txt', 'w') as file:
            colors = re.findall(r'\#[0-9a-f]{6}', data)
            for color in colors:
                file.write(color + '\n')