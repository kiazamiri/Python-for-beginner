# This Project take a string from user and prints it backwards.


def rev_word(a):
    a.reverse()
    str1 = ' '.join(a)
    print(str1)


words = input("Please enter your string: ")
a = words.split()
rev_word(a)
