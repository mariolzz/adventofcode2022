input_file = open("input.txt", "r")

elves = []
elf = []
sums = []

for num in input_file.readlines():
    if num != "\n":
        elf.append(int(num))
    
    else:
        elves.append(elf)
        elf = []
        
for elf in elves:
    sum = 0
    for calories in elf:
        sum += calories
    sums.append(sum)
    
sums.sort()

res1 = max(sums)

res2 = sums[-1] + sums[-2] + sums[-3]

print("Result 1: ", res1)
print("Result 2: ", res2)
