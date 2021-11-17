"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}

* (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
"""
test_list_thesaurus = ["Иван", "Мария", "Петр", "Илья"]
test_list_thesaurus_adv = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]


def thesaurus(*args):
    """
    Creating dictionary: key - name first symbol
    distributes input arguments into the dictionary
    :param args: Names in format "Name"
    :return: Dictionary
    """
    output = {}
    for arg in args:
        if not(output.get(arg[0])):
            output[arg[0]] = [arg]
        else:
            output[arg[0]].append(arg)
    return output


def thesaurus_adv(*args):
    """
    Creating dictionary of dictionaries: first key - surname first symbol, second key: name first symbol
    distributes input arguments into the dictionary
    :param args: Names in format "Name Surname"
    :return: Dictionaries in dictionary
    """
    output = {}
    for arg in args:
        name, surname = arg.split(' ')
        if not(output.get(surname[0])):
            output[surname[0]] = {}
        if not(output[surname[0]].get(name[0])):
            output[surname[0]][name[0]] = [arg]
        else:
            output[surname[0]][name[0]].append(arg)
    return output


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
