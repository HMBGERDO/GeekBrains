"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в
ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
использовать в ответе функции?
"""

import requests

money_transfer = {}

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
date = response.headers['Date']
encoding = requests.utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encoding)
for el in (content.split('<Valute ID=')[1:]):
    key = el[el.index('<CharCode>') + 10:el.index('</CharCode>')]
    value = el[el.index('<Value>') + 7:el.index('</Value>')]
    value = float('{}.{}'.format(value[:value.index(',')], value[value.index(',') + 1:]))
    printname = el[el.index('<Name>') + 6:el.index('</Name>')]
    money_transfer[key] = {
        'value': value,
        'printname': printname,
    }


def print_transfer_amount(key):
    """
    Prints name of currency and transfer amount
    :param key: currency Key
    :return: transfer amount, date
    """
    key = key.upper()
    info = money_transfer.get(key)
    if not info:
        print('No information about {} currency key'.format(key))
        return None
    else:
        print('{} : {} at {}'.format(info['printname'], info['value'], date))
        return info['value'], date


if __name__ == '__main__':
    print_transfer_amount('USD')
    print_transfer_amount('EUR')
