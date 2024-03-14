# Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact та UpdateContact.
import inspect


class Contact:
    f = 15

    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        pass

    def sent_message(self):
        pass


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        pass


contact1 = Contact("surname3", "name3", 20, 3803, "3@gmail.com")
contact2 = Contact("surname4", "name4", 21, 3804, "4@gmail.com")
up_contact1 = UpdateContact("surname1", "name1", 18, 3801, "1@gmail.com", "job1")
up_contact2 = UpdateContact("surname2", "name2", 19, 3802, "2@gmail.com", "job2")

dir_contact = dir(Contact)

print([method for method in dir(Contact) if callable(getattr(Contact, method))])
for i in dir(Contact):
    if callable(getattr(Contact, i)):
        print(i)
    else:
        print(f"{i} не метод")
