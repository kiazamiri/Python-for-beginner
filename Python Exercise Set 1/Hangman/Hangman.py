# This project is the Hangman Game. The computer picks a random
# name from the sowpods.txt folder.

import random


def pick_random_word():
    counter_dict = []
    with open('sowpods.txt') as f:
        line = f.readline()
        while line:
            line = line.strip()
            counter_dict.append(line)
            line = f.readline()
    word = random.choice(counter_dict)
    return word


def ask_user_for_next_letter():
    letter = input("Guess your letter: ")
    return letter.strip().upper()


def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return " ".join(output)


if __name__ == '__main__':
    WORD = pick_random_word()

    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0

    print("Welcome to Hangman!")
    while (len(letters_to_guess) > 0) and num_guesses < 6:
        guess = ask_user_for_next_letter()

        # check if we already guessed that
        # letter
        if guess in correct_letters_guessed or \
                guess in incorrect_letters_guessed:
            # print out a message
            print("You already guessed that letter.")
            continue

        # if the guess was correct
        if guess in letters_to_guess:
            # update the letters_to_guess
            letters_to_guess.remove(guess)
            # update the correct letters guessed
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            # only update the number of guesses
            # if you guess incorrectly
            num_guesses += 1

        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left".format(6 - num_guesses))

    # tell the user they have won or lost
    if num_guesses < 6:
        print("Congratulations! You correctly guessed the word {}".format(WORD))
    else:
        print("Sorry, you list! Your word was {}".format(WORD))
