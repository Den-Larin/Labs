from user import User
class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges(['Allowed to add message', 'Allowed to delete users', 'Allowed to ban users'])

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print('Привілеї адміністратора:')
        for privilege in self.privileges:
            print(f'{privilege}')

admin = Admin('Jack', 'Lewis', 25, 'USA')
admin.privileges.show_privileges()
