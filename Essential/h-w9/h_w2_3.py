from h_w2_1 import int_type

while True:
    print("Вихід - 0")
    num1 = input("Введіть ціле число для додавання: ")
    if num1 == 0:
        break
    num1 = int_type(num1)
    num2 = input("Введіть ціле число для додавання: ")
    num2 = int_type(num2)
    print(num1 + num2)
