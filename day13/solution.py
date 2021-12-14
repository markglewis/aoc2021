import numpy as np

def foldhorizontal(m, y,maxy):
    
    a = m[0: y, :]
    b = m[y+1:,:]
    b = np.flipud(b)
    if a.shape[0] == b.shape[0]:
        #print(1)
        m = a+b
    elif a.shape[0] > b.shape[0]:
        #print(2)
        while a.shape[0] != b.shape[0]:
            b = np.insert(b,0,np.zeros(b.shape[1], dtype = int),0)
        m = a+b
        
    elif a.shape[0] < b.shape[0]:
        #print(3)
        while a.shape[0] != b.shape[0]:
            a = np.insert(a,0,np.zeros(b.shape[1], dtype = int),0)
        m = a+b
    return m

def foldvertival(m, x, maxx):
    a = m[:, :x]
    b = m[:,x+1:]
    a = np.fliplr(a)
    if a.shape[1] == b.shape[1]:
        #print(4)
        m = a+b
    elif a.shape[1] > b.shape[1]:
        #print(5)
        while a.shape[1] != b.shape[1]:
            
            b = np.append(b, np.zeros((b.shape[0],1), dtype=int) , axis=1)
        m = a+b
        
    elif a.shape[1] < b.shape[1]:
        #print(6)
        while a.shape[1] != b.shape[1]:
            a = np.append(a, np.zeros((a.shape[0],1), dtype=int) , axis=1)
        m = a+b
    return m

def inverse():
    return

file1 = open('input.txt', 'r')
coors = []
maxx = 0
maxy = 0
instructions = []
coordinatesinput = True
while True:


    line = file1.readline()

    if not line:
        break

    line = line.strip('\n')
    if line == '':
        coordinatesinput = False

    else:
        if coordinatesinput:
            line = line.split(",")
            line = list(map(int, line))
            coors.append((line[0],line[1]))
            if line[0] > maxx:
                maxx = line[0]
            if line[1] > maxy:
                maxy = line[1]
        else:
            line = line.split(" ")
            line = line[2]
            line = line.split("=")
            instructions.append((line[0],int(line[1])))

 
file1.close()


m = np.zeros([maxy+1, maxx+1])
for i in coors:
    m[i[1],i[0]] = 1
'''
part1 = instructions[0]
if part1[0] == 'x':
    m = foldvertival(m, part1[1],maxx)
elif part1[0] == 'y':
    m = foldhorizontal(m , part1[1],maxy)
count = 0
for (x,y), value in np.ndenumerate(m):
    if m[x,y] != 0:
        count += 1
print(m)
print(count)
'''

print(m.shape)
for i in instructions:
    if i[0] == 'x':
        m = foldvertival(m, i[1],maxx)
    elif i[0] == 'y':
        m = foldhorizontal(m , i[1],maxy)
    print(m.shape)
count = 0
for (x,y), value in np.ndenumerate(m):
    if m[x,y] != 0:
        count += 1
print(m)

f = open("out.txt", "a")


outstring = ""
storedx = 0
for (x,y), value in np.ndenumerate(m):
    if x > storedx:
        outstring+= "\n"
        storedx = x
    if value == 0:
        outstring+= " "
    else:
        outstring+="1"
f.write(outstring)
f.close()