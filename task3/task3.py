# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад
# менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

file = open('file3.txt', 'r', encoding='utf-8')
content = file.readlines()
print(content)
salary = 0
count = 0
persons = []
for line in content:
    print(line)
    salary_item = line.split(' ')
    if int(salary_item[2]) <= 20000:
        persons.append(salary_item[0])
    salary += int(salary_item[2])
    count += 1
result = salary / count
print(f"Сотрудники, получающие менее 20000 руб.: {persons}")
print(f"Средняя зарплата сотрудников: {result}")
file.close()
