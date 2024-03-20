# # 2. Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл

# version 1
def gerator(list1):
    """виводе список квадратів парних чисел"""
    print("version1")
    index = 0
    while index < len(list1):
        if list1[index] % 2 == 0:
            yield list1[index] ** 2
            index += 1
        else:
            index += 1


for j in gerator([1, 5, 10, 12, 14, 2, 3, 4, 5]):
    print(j)

print()
print("version2")

# version 2
list_num = [1, 5, 10, 12, 14, 2, 3, 4, 5]
for x in list_num:
    if x % 2 == 0:
        print(x ** 2)

print()
print("version3")


# version 3
class Iterat:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.iter_obj):
            raise StopIteration
        else:
            if self.iter_obj[self.index] % 2 == 0:
                result = self.iter_obj[self.index]
                self.index += 1
                return result ** 2
            else:
                self.index += 1
                return next(self)


for i in Iterat(list_num):
    print(i)
