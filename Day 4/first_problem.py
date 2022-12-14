input_file = open("input.txt")

pairs = 0

for line in input_file.readlines():

    first_pair, second_pair = line.split(",")

    first_range_l, first_range_r = first_pair.split("-")
    second_range_l, second_range_r = second_pair.split("-")

    print(first_range_l, first_range_r)
    print(second_range_l, second_range_r)

    if int(first_range_l) in range(int(second_range_l), int(second_range_r)+1) and int(first_range_r) in range(int(second_range_l), int(second_range_r)+1):
        pairs += 1
        print("PAIR")

    elif int(second_range_l) in range(int(first_range_l), int(first_range_r)+1) and int(second_range_r) in range(int(first_range_l), int(first_range_r)+1):
        pairs += 1
        print("PAIR")

    print("------------------")

print(pairs)
