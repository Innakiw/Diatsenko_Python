# п.2 Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так, щоб він зберігав
# базу посилань на диску і не «забув» при перезапуску. За бажанням можете ознайомитися з модулем shelve
# (https://docs.python.org/3/library/shelve.html), який у даному випадку буде дуже зручним та спростить виконання
# завдання.
#
# Створіть програму, яка емулює роботу сервісу зі скорочення посилань.
# # Повинна бути реалізована можливість введення початкового посилання та короткої назви
# # і отримання початкового посилання за її назвою.


import shelve

import shelve

with shelve.open("Links") as f:
    link = {}
    while True:
        answer = input("Для того щоб ввести посилання введіть 1. Для отримання посилання введіть 2: \n")
        if answer == "0":
            break
        elif answer == "1":
            new_name_link = input("Введіть коротку назву посилання: ")
            new_link = input("Введіть посилання: ")
            f[new_name_link] = new_link
        elif answer == "2":
            list_links = []
            with shelve.open("Links") as f:
                for key, val in enumerate(f):
                    print(f"{key + 1}. {val}")
                    list_links.append(f[val])
                link_choose = input("Введіть номер посилання: > ")
                link_choose = int(link_choose)
                if link_choose <= len(list_links) and link_choose != 0:
                    print(list_links[link_choose - 1])
                    print(list_links)
                else:
                    print("Ви ввели невірний номер посилання")
        else:
            print("Ви ввели неіснуючий номер дії яку хочете виконати")
