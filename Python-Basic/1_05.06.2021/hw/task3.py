'''
Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
'''
declension = []
declension.append('процент')
for i in range(1, 4):
    declension.append('процента')
for i in range(1, 17):
    declension.append('процентов')
for i, v in enumerate(declension):
    print('{} {}'.format(i + 1, v))
