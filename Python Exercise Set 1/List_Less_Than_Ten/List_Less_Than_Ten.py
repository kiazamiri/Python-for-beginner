# This project will get a number from the user and prints the
# numbers in the list that are less than it (in a separate list).

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input('Please enter your number: '))
num = []
for x in a:
    if x < number:
        num.append(x)
print(num)
