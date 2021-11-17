import sys

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write('{}\n'.format(sys.argv[1]))