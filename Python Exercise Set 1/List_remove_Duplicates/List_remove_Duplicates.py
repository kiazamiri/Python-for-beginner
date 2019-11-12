# This project removes duplicates in a list.


def dup_remove(a):
    uniq = []
    for x in a:
        if x not in uniq:
            uniq.append(x)
    uniq.sort()
    print(uniq)


a = [1, 2, 1, 23, 15, 46, 46, 75, 631, 158, 33, 33, 55]
dup_remove(a)
