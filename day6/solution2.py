file1 = open('input.txt', 'r')

lanternfishlist = []
while True:


    line = file1.readline()

    if not line:
        break

    lanternfishlist = line.split(',')
 
file1.close()
lanternfishlist = list(map(int, lanternfishlist))
print(lanternfishlist)

days = 0
lanternfish = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}


for i in lanternfishlist:
    lanternfish[i] = lanternfish[i] + 1

while days < 256:
    #print(lanternfish)
    newlanters = lanternfish[0]
    lanternfish[0],lanternfish[1], lanternfish[2],lanternfish[3],lanternfish[4],lanternfish[5], lanternfish[6],lanternfish[7] = lanternfish[1], lanternfish[2],lanternfish[3],lanternfish[4],lanternfish[5], lanternfish[6],lanternfish[7],lanternfish[8]
    lanternfish[8] = newlanters
    lanternfish[6] = lanternfish[6] + newlanters
    print(days)
    print(lanternfish.items())
    
    days+=1
print(sum(lanternfish.values()))
