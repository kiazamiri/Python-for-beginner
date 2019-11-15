# This project gets a number from the user and searchs a list
# to find whether or not is it in the list.


def search(order_list, number):
    if number in order_list:
        return True
    else:
        return False


a = [2, 3, 10, 14, 15, 16, 20, 23]
num = int(input("Please enter your number: "))
search(a, num)
