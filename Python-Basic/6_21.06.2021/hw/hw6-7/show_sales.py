import sys

if len(sys.argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            print(line)
elif len(sys.argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        arr = f.read().split('\n')
        for i in arr[int(sys.argv[1]):]:
            print(i)
elif len(sys.argv) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for i in arr[int(sys.argv[1]):int(sys.argv[2]) + 1]:
            print(i)
