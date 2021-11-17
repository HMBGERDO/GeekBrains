name = 'Basil'
surname = 'Ivanov'
age = 29

user_info = [name, surname, age]

print('Surname: ', user_info[1])

user_info = {
    'name' : name,
    'surname' : surname,
    'age' : age,
    'education' : ['MSU', 'HSE'],
    'in_army': True,
}
print(user_info['education'])

user_info['job'] = 'BookShop'

print(user_info)

army = {
    'in_army': False,
    'suitable': True,
    'test': None,
}
user_info.update(army )

print(army['test'])
print(user_info)
print(''.isupper())
print('s'.isupper())
print('S'.isupper())