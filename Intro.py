class User: 
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def show_age(self):
        print('I have no age')


class AgedUser(User):
    age:int

    def __init__(self, first_name, last_name,age):
        super().__init__(first_name, last_name)
        self.age=age

    def full_name_with_age(self):
        return super().full_name() + ' ' + str(self.age)

    def show_age(self):
        print(self.age)

NewUser = AgedUser('John','Doe',30)

print(NewUser.full_name_with_age())



NewUser = User('Artur','Doe')
NewUser.show_age()