# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

print('Введите данные: ')
user_strings = []
i = True
while i:
    i = input()
    if i:
        user_strings.append(i)

data = open('file.txt', 'w', encoding='utf-8')
data.writelines(user_strings)
data.close()