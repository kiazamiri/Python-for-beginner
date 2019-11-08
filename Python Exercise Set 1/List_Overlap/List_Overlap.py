# This project generates two list of random integers with different
# sizes of 10 and 13. Then returns a list that contains the similar
# numbers between them without duplicates.

from random import randint

a = []
b = []
num = []
uniq = []
for x in range(1, 10):
    a_list = randint(0, 100)
    a.append(a_list)
print(sorted(a))

for x in range(1, 13):
    b_list = randint(0, 100)
    b.append(b_list)
print(sorted(b))

for x in a:
    for y in b:
        if y == x:
            num.append(y)
for x in num:
    if x not in uniq:
        uniq.append(x)
print(sorted(uniq))
