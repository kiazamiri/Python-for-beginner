# This Project reads a file full of name and counts how many times each name appeared in it.

counter_dict = {}
with open('nameslist.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = f.readline()

print(counter_dict)
