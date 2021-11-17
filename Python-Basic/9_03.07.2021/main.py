class Printer:
    def print_attributes(self):
        print(self.__dict__)


class User(Printer):
    workplace = 'Third floor office'
    __tab = []

    # def get_data(self):
    #     self.name = input('Name: ')
    #     self.surname = input('Surname: ')
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def _update_work_tab(self, date, on_work, flag):
        if flag == 'Admin':
            self.__tab.append((date, on_work))


class Admin(Printer):
    def check_worker_presence(self, user: User, date, on_work):
        user._update_work_tab(date, on_work, flag='Admin')


user1 = User('Basil', 'Vasil')
admin = Admin()
user1.print_attributes()
admin.print_attributes()
admin.check_worker_presence(user1, '02.05.2021', True)
print(user1._User__tab)
