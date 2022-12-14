input_file = open("input.txt")

total_points = 0

for line in input_file.readlines():
    line = line.replace("\n", "")

    other, me = line.split(" ")

    match other:
        case "A":
            match me:
                case "X":
                    total_points += 3 + 1
                case "Y":
                    total_points += 6 + 2
                case "Z":
                    total_points += 0 + 3
        case "B":
            match me:
                case "X":
                    total_points += 0 + 1
                case "Y":
                    total_points += 3 + 2
                case "Z":
                    total_points += 6 + 3
        case "C":
            match me:
                case "X":
                    total_points += 6 + 1
                case "Y":
                    total_points += 0 + 2
                case "Z":
                    total_points += 3 + 3

print(total_points)
