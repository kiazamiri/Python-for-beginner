# This project gets a number from the user and collects all the
# divisors of that number in a separate list and prints them.

num = int(input('Please enter your number: '))
numbers = []
for x in range(1, num+1):
    if num % x == 0:
        numbers.append(x)
print(numbers)
