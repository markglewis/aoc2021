file1 = open('input.txt', 'r')

lanternfish = []
while True:


    line = file1.readline()

    if not line:
        break

    lanternfish = line.split(',')
 
file1.close()
lanternfish = list(map(int, lanternfish))

days = 0


while days < 100:
    fishToAdd = []
    for fish in range(len(lanternfish)):
        if lanternfish[fish] != 0:
            lanternfish[fish] = lanternfish[fish] -1
        else:
            lanternfish[fish] = 6
            fishToAdd.append(8)
    lanternfish = lanternfish + fishToAdd
    fishToAdd = []
    #print(days)
    #print(lanternfish)
    days +=1
    print(len(lanternfish))

print(len(lanternfish))