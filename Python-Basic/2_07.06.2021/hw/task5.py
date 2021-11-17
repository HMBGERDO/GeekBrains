'''
Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
* Вывести на экран эти цены через запятую в одну строку,
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

* Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
* Создать новый список, содержащий те же цены, но отсортированные по убыванию.
* Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
'''


def format_money(money):
    money = str(money)
    if money.count('.') == 0:
        output = ' '.join([money, 'руб 00 коп'])
    elif len(money[money.index('.') + 1:]) < 2:
        output = ' '.join([money[:money.index('.')], 'руб', (''.join([money[money.index('.') + 1:], '0'])), 'коп'])
    else:
        output = ' '.join([money[:money.index('.')], 'руб', money[money.index('.') + 1:], 'коп'])
    return output


def printprices(message, prices):
    output_arr = []
    for i in prices:
        output_arr.append(format_money(i))
    print(message, ', '.join(output_arr))


prices = [57.8, 46.51, 97, 195, 0.02, 13]

printprices('Цены без сортировки:', prices)
prices.sort()
printprices('Сортировка по возрастанию:', prices)
new_prices = prices.copy()
new_prices.sort(reverse=True)
printprices('Сортировка по убыванию:', new_prices)
printprices('Пять самых высоких цен:', prices[len(prices) - 5:])
