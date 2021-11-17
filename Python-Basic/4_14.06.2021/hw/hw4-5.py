"""
4. Написать свой модуль my_utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт, в
котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего лишнего
не происходит.
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

import my_utils, sys

if len(sys.argv) > 1:
    name, val, date = my_utils.main.transfer_amount(sys.argv[1])
    print('{} {}'.format(val, date))

# print(my_utils.main.transfer_amount('USD'))