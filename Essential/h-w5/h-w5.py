# п.5 Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact
# та їх екземплярах. Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів. Порівняйте їх.
# Зробіть відповідні висновки.

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
up_contact1 = UpdateContact("surname1", "name1", 18, 3801, "1@gmail.com", "job1")

print(f"Class Contact: {dir(Contact)}")
print(f"Class UpdateContact and job:{dir(UpdateContact)}")
print(f"contact1: {dir(contact1)}")
print(f"up_contact1 and job: {dir(up_contact1)}")
delattr(up_contact1, "job")
print(f"Class Contact: {dir(Contact)}")
print(f"Class UpdateContact del job: {dir(UpdateContact)}")
print(f"contact1: {dir(contact1)}")
print(f"up_contact1 del job: {dir(up_contact1)}")
