import statistics
file1 = open('input.txt', 'r')

def getcost(x, points):
    total = 0
    for i in points:
        total += abs(x-i)
    return total



points = []
while True:
    line = file1.readline()
    if not line:
        break

    
    points = line.split(',')

file1.close()
points = list(map(int, points))

costs = {}
for i in range(max(points)):
    costs[i] = getcost(i,points)
print(costs)

lowest_val = None

for key, val in costs.items():
    if lowest_val == None:
        lowest_val = (key,val)
    else:
        if val < lowest_val[1]:
            lowest_val = (key,val)

print(lowest_val)