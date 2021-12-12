def incrementstep(key,flashed,graph):
    
    if key not in flashed:  
        graph[key] = graph[key] + 1
        
        if graph[key] > 9:
            graph[key] = 0
            flashed.append(key)
            neighbors = getadjacent(key,graph)
            print(key)
            print(neighbors)
            for i in neighbors:
                graph,flashed = incrementstep(i,flashed,graph)
    return (graph,flashed)

def getadjacent(key,graph):
    valid = []
    potential = [(key[0]-1,key[1]-1),(key[0],key[1]-1),(key[0]+1,key[1]-1),(key[0]-1,key[1]),(key[0]+1,key[1]),(key[0]-1,key[1]+1),(key[0],key[1]+1),(key[0]+1,key[1]+1)]
    for i in potential:
        if i in graph.keys():
            valid.append(i)
    return valid
file1 = open('input.txt', 'r')

def graphprint(graph):
    printstring = ""
    currentrow = 0
    for key, value in graph.items():
        if currentrow != key[1]:
            currentrow +=1
            printstring += "\n"
        printstring += str(value)
    printstring += "\n"
    print(printstring)


graph = {}
col = 0
while True:


    line = file1.readline()

    if not line:
        break

    for idx , val in enumerate(line):
        if val != "\n":
            graph[(idx,col)] = int(val)
    col += 1
file1.close()


total = 0
step = 0
allflash = []
while step < 500:
    step += 1
    flashed = []
    for key,value in graph.items():
        graph,flashed = incrementstep(key,flashed,graph)
    
    total += len(flashed)

    if len(flashed) == len(graph):
        graphprint(graph)
        allflash.append(step)
    
print(total)
print(allflash)