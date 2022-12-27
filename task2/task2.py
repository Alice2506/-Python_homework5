# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('file2.txt', 'r', encoding='utf-8')
lines = 0
words = 0

for line in file:
    lines += 1
    words += len(line.split())

print("Lines:", lines)
print("Words:", words)

