class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0
    def describe_user(self):
        print(self.first_name, self.last_name)
    def greeting_user(self):
        print(f"Вітаємо, {self.first_name}, {self.last_name}")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Denis', 'Larin', 18, 'Ukraine')
user2 = User('Mychailo', 'Kormosh', 19, 'Ukraine')
user3 = User('Jon', 'Williams', 21, 'Great Britain')

print('Завдання a:')
user1.describe_user()
user1.greeting_user()
user2.describe_user()
user2.greeting_user()
user3.describe_user()
user3.greeting_user()

print('Завдання b:')
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
