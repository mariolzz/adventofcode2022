input_file = open("input.txt")

stacks = [
    ["H", "T", "Z", "D"],
    ["Q", "R", "W", "T", "G", "C", "S"],
    ["P", "B", "F", "Q", "N", "R", "C", "H"],
    ["L", "C", "N", "F", "H", "Z"],
    ["G", "L", "F", "Q", "S"],
    ["V", "P", "W", "Z", "B", "R", "C", "S"],
    ["Z", "F", "J"],
    ["D", "L", "V", "Z", "R", "H", "Q"],
    ["B", "H", "G", "N", "F", "Z", "L", "D"]
]


for line in input_file.readlines():

    tokens = line.split(" ")

    move = int(tokens[1])
    from_pos = int(tokens[3]) - 1
    to_pos = int(tokens[5]) - 1

    popped_list = []

    for i in range(move):
        popped_list.append(stacks[from_pos].pop())

    popped_list.reverse()

    stacks[to_pos] = stacks[to_pos] + popped_list

output = ""

for stack in stacks:
    output += stack[-1]

print(output)
