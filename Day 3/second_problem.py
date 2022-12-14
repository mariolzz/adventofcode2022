input_file = open("input.txt")

group = []
total = 0

for line in input_file.readlines():

    group.append(set(line.strip()))

    if len(group) == 3:
        inter = ''.join(group[0].intersection(group[1]).intersection(group[2]))

        if inter.isupper():
            total += ord(inter) - 38

        elif inter.islower():
            total += ord(inter) - 96

        group = []

print(total)
