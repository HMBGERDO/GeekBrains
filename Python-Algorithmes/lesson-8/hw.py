# Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции дана строка,
# требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
def substrings_counter(string, mode=False):
    result = {}
    for i in range(1, len(string)):
        if mode and i > 1:
            break
        for j in range(0, len(string) - i + 1):
            current_part = string[j:j+i]
            if current_part in result:
                continue
            current_hash = hash(string[j:j+i])
            for t in range(j + 1, len(string) - i + 1):
                if hash(string[t:t+i]) == current_hash:
                    if current_part not in result:
                        result[current_part] = 2
                    else:
                        result[current_part] += 1
    return result


print(substrings_counter('apple and pineapple'))
# Закодировать любую строку по алгоритму Хаффмана.
# apple and pineapple
# p-5 - 00
# a-3 - 010
# e-3 - 011
# l-2 - 100
# ' '-2 - 101
# n-2 - 110
# d-1 - 1110
# i-1 - 1111
# apple and pineapple - 010 00 00 100 011 101 010 110 1110 101 00 1111 110 011 010 00 00 100 011
