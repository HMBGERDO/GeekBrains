"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""

translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

testwords = [
    'one',
    'One',
    'eight',
    'Ten',
]


def num_translate(num):
    """
    Printing translated input number using translate dictionary
    :param num: number to translate
    :return: None
    """
    if translate.get(num):
        print(translate[num])


def num_translate_adv(num):
    """
    Printing translated input number using translate dictionary with first upper or lower symbol
    :param num: number to translate
    :return: None
    """
    cap = num[0].isupper()
    if translate.get(num.lower()):
        if cap:
            print(translate[num.lower()].capitalize())
        else:
            print(translate[num.lower()])


for word in testwords:
    print('{} num_translate: '.format(word))
    num_translate(word)
    print('{} num_translate_adv: '.format(word))
    num_translate_adv(word)
    print('')
