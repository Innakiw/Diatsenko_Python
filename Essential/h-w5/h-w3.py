# п.3 Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr().
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.

class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        print("get_contact")

    def sent_message(self):
        print("sent_message")


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

print(hasattr(contact1, "surname"))
print(getattr(contact1, "surname"))
setattr(contact1, "surname", "surname33")
print(getattr(contact1, "surname"))
delattr(contact1, "surname")
print(hasattr(contact1, "surname"))

print()
print(hasattr(contact1, "name"))
print(getattr(contact1, "name"))
setattr(contact1, "name", "name33")
print(getattr(contact1, "name"))
delattr(contact1, "name")
print(hasattr(contact1, "name"))

print()
print(hasattr(contact1, "age"))
print(getattr(contact1, "age"))
setattr(contact1, "age", "30")
print(getattr(contact1, "age"))
delattr(contact1, "age")
print(hasattr(contact1, "age"))

print()
print(hasattr(contact1, "mob_phone"))
print(getattr(contact1, "mob_phone"))
setattr(contact1, "mob_phone", "38033")
print(getattr(contact1, "mob_phone"))
delattr(contact1, "mob_phone")
print(hasattr(contact1, "mob_phone"))

print()
print(hasattr(contact1, "email"))
print(getattr(contact1, "email"))
setattr(contact1, "email", "33@gmail.com")
print(getattr(contact1, "email"))
delattr(contact1, "email")
print(hasattr(contact1, "email"))
print()
print(contact1.__dict__)


print()
print(hasattr(Contact, "get_contact"))
setattr(Contact, "get_contact", "get_contact33")
print(hasattr(Contact, "get_contact"))
print(getattr(Contact, "get_contact"))
delattr(Contact, "get_contact")
print(hasattr(Contact, "get_contact33"))
print(dir(Contact))


print()
print(hasattr(Contact, "sent_message"))
setattr(Contact, "sent_message", "sent_message33")
print(hasattr(Contact, "sent_message"))
print(getattr(Contact, "sent_message"))
delattr(Contact, "sent_message")
print(hasattr(Contact, "sent_message"))
print(dir(Contact))




