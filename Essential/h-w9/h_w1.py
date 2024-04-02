# Перепишіть домашнє завдання попереднього уроку (сервіс для скорочення посилань) таким чином, щоб у нього була основна
# частина, яка відповідала би за логіку роботи та надавала узагальнений інтерфейс, і модуль представлення,
# який відповідав би за взаємодію з користувачем. При заміні останнього на інший, який взаємодіє з користувачем в інший
# спосіб, програма має продовжувати коректно працювати.

import shelve


def write_shelve():
    with shelve.open("Links") as f:
        new_name_link = input("Введіть коротку назву посилання: ")
        new_link = input("Введіть посилання: ")
        f[new_name_link] = new_link


def get_list_links():
    list_links = []
    with shelve.open("Links") as f:
        for key, val in enumerate(f):
            # print(f"{key + 1}. {val}")
            list_links.append(val)
    return list_links


def get_full_link(short_link):
    with shelve.open("Links") as f:
        full_link = f[short_link]
        return full_link
