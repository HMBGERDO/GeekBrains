a = [i**3 for i in range(128) if i % 8 == 0]

def b(num):
    for i in range(128):
        yield i**3

gen = b(10)

for i in range(129):
    print(next(gen))
