import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    arr = f.read().split('\n', int(sys.argv[1]))
    try:
        arr[int(sys.argv[1]) - 1]
    except IndexError:
        print('List out of range')
        f.close()
    arr[int(sys.argv[1]) - 1] = sys.argv[2]
    with open('bakery.csv', 'w', encoding='utf-8') as file:
        for sale in arr[:-1]:
            file.write('{}\n'.format(sale))
        file.write('{}'.format(arr[-1]))
