# This project is the guessing game. Where the user picks a number
# and the computer will guess it. The final number and the number
# guessed will be printed at the end.

print("Welcome to the guessing game. Please pick a number.\n")
guess = 50
var = 50
count = 0
while True:
    a = input(f"Is your number lower or higher than {guess} (h/l)? ")
    if a.lower() == "l":
        guess = guess - int((var / 2) + 1)
        var = var/2
        count += 1
    elif a.lower() == "h":
        guess = int((var / 2) + 1) + guess
        var = var/2
        count += 1
    b = input(f"Is your number {guess} (y/n)? ")
    if b.lower() == "y":
        break

print(f"The number of Guesses: {count}")
print(f"Your number is {guess}")
