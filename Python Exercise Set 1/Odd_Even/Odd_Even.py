# In this exercise we ask to number from the user and the result
# will determine whether it able to be divided or not by Check
# Number.

num = int(input('Please enter your number: '))
check = int(input('Please enter your divide number: '))

if num % check != 0:
    print(num, 'is not a multiple of', check, '.')
else:
    print(num, 'is a multiple of', check, '.')

# The code below is the initial step for the code above:
# number = int(input('Please enter your number: '))
# if number % 4 == 0:
#     print(number, "is a multiple of 4.")
# elif number % 2 != 0:
#     print(number, "is Odd.")
# else:
#     print(number, "is Even.")
