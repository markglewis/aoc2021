file1 = open('input.txt', 'r')

temp = None
increased = 0
while True:


    line = file1.readline()

    if not line:
        break

    if temp != None:
        if int(line) > temp:
            increased +=1
    
    temp = int(line)
 
file1.close()
print(increased)