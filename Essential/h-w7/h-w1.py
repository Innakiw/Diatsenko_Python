# п.1 Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

def generator(list1):
    """повертає елементи заданого списку у зворотному порядку"""
    index = len(list1) - 1
    while index >= 0:
        yield list1[index]
        index -= 1


for i in generator(["dsf", 2, 3, 4, 5, 6]):
    print(i)
