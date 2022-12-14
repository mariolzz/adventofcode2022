input_file = open("input.txt")

total = 0

for line in input_file.readlines():

    length = len(line)

    left = line[:length//2]
    right = line[length//2:]

    for char1 in right:
        if char1 in left:
            if char1.isupper():
                total += ord(char1) - 38

            elif char1.islower():
                total += ord(char1) - 96

            break

print(total)
