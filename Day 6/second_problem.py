def check_unique(packet):
    for i in range(len(packet)):
        for j in range(i+1, len(packet)):
            if packet[i] == packet[j]:
                return False

    return True


input_file = open("input.txt")

line = input_file.readline().strip()

packets = [line[i:i+14] for i in range(0, len(line), 1)]

first_packet = packets[0]

for packet in packets:
    if check_unique(packet):
        first_packet = packet
        break

print(first_packet)
print(line.find(first_packet) + 14)
