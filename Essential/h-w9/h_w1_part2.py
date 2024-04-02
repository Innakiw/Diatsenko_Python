import h_w1

while True:
    answer = input("Для того щоб ввести посилання введіть 1. Для отримання посилання введіть 2, 0 - Вихід: \n")
    if answer == "0":
        break
    elif answer == "1":
        h_w1.write_shelve()
    elif answer == "2":
        list_links = h_w1.get_list_links()
        for idx, val in enumerate(list_links):
            print(f"{idx + 1}. {val}")
        link_choose = input("Введіть номер посилання: > ")
        link_choose = int(link_choose)
        if link_choose > len(list_links) or link_choose == 0:
            print("Ви ввели номер посилання, що не існує")
            continue

        value = list_links[link_choose - 1]
        print(value)
        full_link_print = h_w1.get_full_link(value)
        print(full_link_print)
    else:
        print("Ви ввели неіснуючий номер дії яку хочете виконати")
