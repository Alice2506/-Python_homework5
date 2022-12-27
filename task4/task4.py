# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
result = []
file = open("file4.txt", 'r', encoding='utf-8')
for line in file:
    item = line.split(" - ")
    line.strip()
    print(line)
    if item[0] in dict:
        word = dict[item[0]]
        result.append(word +' - '+ item[1])
print(result)
for el in result:
    print(el)
file.close()

with open("new_file.txt", "w", encoding='utf-8') as result_file:
    for el in result:
        print(el, file=result_file)



