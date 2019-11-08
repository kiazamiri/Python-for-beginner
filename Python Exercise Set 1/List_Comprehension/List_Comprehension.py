from random import randint

list1 = []
list_length = randint(10, 15)

while len(list1) < list_length:
    list1.append(randint(1, 100))

even_list = [num for num in list1 if num % 2 == 0]

print(list1)
print(even_list)