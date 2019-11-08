# This Project aks the user their name and age, then prints the
# statement for number of repeat times addressing them what year
# they will turn 100

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
repeat = int(input('Please enter how times you want to repeat: '))

age_2 = 2019 - age + 100
while repeat > 0:
    print(f'{name}, you will turn 100 in the year {age_2}\n')
    repeat -= 1
