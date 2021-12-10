def getNeighbors(key,graph):
    x = key[0]
    y = key[1]
    neighbors = []

    potential_neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    for i in potential_neighbors:
        if i in graph:
            neighbors.append(i)



    return neighbors

def islowest(key, neighbors, graph):
    for i in neighbors:
        if graph[key] >= graph[i]:
            return False
    return True

def dfs(visited, graph, key):
    if key not in visited:
        visited.add(key)
        neighbors = getNeighbors(key,graph)
        validneighbors = []
        for neighbour in neighbors:
            if graph[neighbour] != 9:
                validneighbors.append(neighbour)
        for neighbour in validneighbors:
            dfs(visited, graph, neighbour)

file1 = open('input.txt', 'r')

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

lowest_points = []
for key in graph.keys():
    if islowest(key, getNeighbors(key,graph), graph):
        lowest_points.append(key)


risklevel = 0
for i in lowest_points:
    risklevel += 1 + graph[i]

print(risklevel)

basinsize = []
for i in lowest_points:
    visited = set()
    basin = dfs(visited,graph,i)
    basinsize.append(len(visited))

basinsize.sort()
print(basinsize[-3:])