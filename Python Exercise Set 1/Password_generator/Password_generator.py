# This project generate a random password for the user with their own length.

import string
import random


def pw_gen(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


print(pw_gen(int(input('How many characters in your password?'))))
