"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в
шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num, repeat=False):
    """
    Creating array of jokes using nouns adverbs and adjectives arrays
    :param num: Integer - how many jokes?
    :param repeat: Boolean - can we repeat words in jokes?
    :return: Array - with jokes or empty array if we cant do it
    """
    current_dict = {
        'nouns': nouns.copy(),
        'adverbs': adverbs.copy(),
        'adjectives': adjectives.copy(),
    }

    if repeat and (len(current_dict['nouns']) < num
                   or len(current_dict['adverbs']) < num
                   or len(current_dict['adjectives']) < num):
        return []
    output = []

    for i in range(num):
        noun = random.choice(current_dict['nouns'])
        adverb = random.choice(current_dict['adverbs'])
        adjective = random.choice(current_dict['adjectives'])
        if repeat:
            current_dict['nouns'].remove(noun)
            current_dict['adverbs'].remove(adverb)
            current_dict['adjectives'].remove(adjective)
        output.append(' '.join([noun, adverb, adjective]))
    return output


print(get_jokes(5, True))
print(get_jokes(128, True))
print(get_jokes(7))
