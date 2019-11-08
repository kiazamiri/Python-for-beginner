# This project checks if the user's number is prime or not.


def prime(number):
    numbers = []
    for x in range(1, number + 1):
        if number % x == 0:
            numbers.append(x)
    if len(numbers) == 1:
        print('1 is not a prime number.')
    elif len(numbers) > 2:
        print(number, 'is not a prime number.')
    else:
        print(number, 'is a prime number.')


while True:
    num = int(input("Please enter your number: "))
    prime(num)
