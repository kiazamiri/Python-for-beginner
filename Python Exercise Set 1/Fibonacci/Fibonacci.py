# This is the Fibonacci function, where the user puts how many
# numbers wants to be generated.


def fibonacci(number):
    count = [1, 1]
    for x in range(0, number-2):
        new_count = count[-1] + count[-2]
        count.append(new_count)

    print(count)


num = int(input("Please enter your number: "))
fibonacci(num)