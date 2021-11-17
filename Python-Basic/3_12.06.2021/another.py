test_list = ['nina', 'katya', 'petya', 'vasya']
print(*map(lambda x: '!{}!'.format(x[:3].upper()), test_list))

print(*filter(lambda x: x.endswith('ya'), test_list))

test_list_surname = ['petrova', 'ivanova', 'koshkin', 'loshkin'] # test
# print(*zip(test_list, test_list_surname))

print(*map(lambda x: '{} {}'.format(x[0].capitalize(), x[1].capitalize()), zip(test_list, test_list_surname)))
