# п.3 Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr().
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.

class Contact:

    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    @staticmethod
    def get_contact():
        print("or")

    @staticmethod
    def sent_message():
        print("and")


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        pass


print(hasattr(Contact, "surname"))
setattr(Contact, "surname", "surname33")
print(hasattr(Contact, "surname"))
print(getattr(Contact, "surname"))
delattr(Contact, "surname")
print(hasattr(Contact, "surname"))

print()
print(hasattr(Contact, "name"))
setattr(Contact, "name", "name33")
print(hasattr(Contact, "name"))
print(getattr(Contact, "name"))
delattr(Contact, "name")
print(hasattr(Contact, "name"))

print()
print(hasattr(Contact, "age"))
setattr(Contact, "age", "age33")
print(hasattr(Contact, "age"))
print(getattr(Contact, "age"))
delattr(Contact, "age")
print(hasattr(Contact, "age"))

print(Contact.__dict__)
print()
print(hasattr(Contact, "mob_phone"))
setattr(Contact, "mob_phone", "mob_phone33")
print('after add: ', dir(Contact))
print(hasattr(Contact, "mob_phone"))
print(getattr(Contact, "mob_phone"))
delattr(Contact, "mob_phone")
print(hasattr(Contact, "mob_phone"))
print(dir(Contact))

print()
print(hasattr(Contact, "email"))
setattr(Contact, "email", "email33")
print(hasattr(Contact, "email"))
print(getattr(Contact, "email"))
delattr(Contact, "email")
print(hasattr(Contact, "email"))

print()
print(dir(Contact))
print(hasattr(Contact, "get_contact"))
setattr(Contact, "get_contact", "get_contact33")
print(hasattr(Contact, "get_contact"))
print(getattr(Contact, "get_contact"))
delattr(Contact, "get_contact")
print(hasattr(Contact, "get_contact33"))
print(dir(Contact))

print()
print(dir(Contact))
print(hasattr(Contact, "sent_message"))
setattr(Contact, "sent_message", "sent_message33")
print(hasattr(Contact, "sent_message"))
print(getattr(Contact, "sent_message"))
delattr(Contact, "sent_message")
print(hasattr(Contact, "sent_message"))
print(dir(Contact))

print()
print(dir(UpdateContact))
print(hasattr(UpdateContact, "get_message"))
setattr(UpdateContact, "get_message", "get_message33")
print(hasattr(UpdateContact, "get_message"))
print(getattr(UpdateContact, "get_message"))
delattr(UpdateContact, "get_message")
print(hasattr(UpdateContact, "get_message"))
print(dir(UpdateContact))
