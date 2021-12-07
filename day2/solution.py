
file1 = open('input.txt', 'r')

depth = 0
horizontal = 0

while True:


    line = file1.readline()

    if not line:
        break

    command = line.split()

    if command[0] == "forward":
        horizontal += int(command[1])
    elif command[0] == "up":
        depth -= int(command[1])
    elif command[0] == "down":
        depth += int(command[1])
 
file1.close()

print(horizontal*depth)