# п.2 Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact, sent_message.
# Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job. Додати методи get_message.
# Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__.
# Роздрукувати інформацію на екрані.
class Contact:
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

print(contact1.__dict__)
print(up_contact1.__dict__)
print(Contact.__base__)
print(UpdateContact.__base__)
print(Contact.__bases__)
print(UpdateContact.__bases__)
