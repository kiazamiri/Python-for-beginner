# This project checks if the users string input is palindrome
# or not.

string = input('Please enter your string: ')
list1 = []
list2 = []
for x in string:
    if x != ' ':
        list1.append(x)
        list2.append(x)
list1.reverse()
if list2 == list1:
    print("This string is palindrome.")
else:
    print("This string is not palindrome.")
