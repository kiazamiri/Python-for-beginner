# In this project the user has to guess a number between 1 to 9
# correctly and at the end their number of guesses is printed.

from random import randint

count = 0
correct = randint(1, 9)
while True:
    guess = input('Please enter your guess or type 0 to quit: ')
    if guess.lower() == 'exit':
        break
    else:
        count += 1
        guess2 = int(guess)
        if guess2 == correct:
            print('You guessed Correctly!! The correct number is ', correct)
            break
        elif guess2 < correct:
            print('Wrong! you guessed lower.')
        elif guess2 > correct:
            print('Wrong! you guessed higher.')


print('You guessed', count, 'times.')
