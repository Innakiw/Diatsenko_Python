# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел. Створіть ще один
# скрипт, який читає числа з файлу та виводить на екран їхню суму.
import random

list_nums = [str(round(random.random() * random.randint(-10000, 10000), 2))  for i in range(1000)]
with open("h-w1", "w") as f:
    f.write(";".join(list_nums))

with open("h-w1", "r") as f:

    list_nums1 = []
    for i in list_nums:
        i = float(i)
        list_nums1.append(i)
    sum =round(sum(list_nums1), 2)
    print(sum)



