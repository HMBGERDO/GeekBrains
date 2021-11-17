'''
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
'''


def makequotes(arr):
    cont = 0
    for k, v in enumerate(arr):
        if cont > 0:
            cont -= 1
            continue
        num = 0
        if v[0] == '+' or v[0] == '-':
            num = 1
        if not (v[num:].isdigit()):
            continue
        if len(v[num:]) == 1:
            arr[k] = ''.join([v[:num], '0', v[num:]])
        else:
            arr[k] = ''.join([v[:num], v[num:]])
        arr.insert(k, '"')
        arr.insert(k + 2, '"')
        cont = 2
    return arr


def printsmart(arr):
    num = 0
    output = ''
    while (arr[num:].count('"') > 0):
        nextquotes = num + arr[num:].index('"')
        buf = ' '.join(arr[num:nextquotes])
        output = ' '.join([output, buf])
        buf = ''.join(arr[nextquotes:nextquotes + 3])
        output = ' '.join([output, buf])
        num = nextquotes + 3
    else:
        buf = ' '.join(arr[num:])
        output = ' '.join([output, buf])

    print(output)


print(makequotes(['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']))

printsmart(makequotes(['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']))
