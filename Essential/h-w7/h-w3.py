# Напишіть функцію-генератор для отримання n перших простих чисел.


def generator(num):
    """функція-генератор для отримання n перших простих чисел"""

    count = 0
    result_qty = 0
    while True:
        count += 1
        if result_qty >= num:
            break

        if count == 0 or count == 1:
            continue

        elif count % 2 == 0 and count != 2:
            continue

        elif count % 5 == 0 and count != 5:
            continue

        else:
            num_count = 0
            for j in range(1, count):
                if count % j == 0:
                    num_count += 1

            if num_count > 2:
                pass
            elif num_count < 2:
                result_qty += 1
                yield count


number = input("Введіть ціле число: ")

try:
    number = int(number)
except ValueError as e:
    print("Введіть ціле число")

for i in generator(number):
    print(i)
