from collections import defaultdict

def traverse(a, seen, can_twice):
    if a == 'end': return 1
    paths = 0
    for b in graph[a]:
        if b.islower():
            if b not in seen:
                paths += traverse(b, seen | {b}, can_twice)
            elif can_twice and b not in {'start', 'end'}:
                paths += traverse(b, seen | {b}, False)
        else:
            paths += traverse(b, seen, can_twice)
    return paths


file1 = open('test.txt', 'r')

graph = defaultdict(list)
while True:


    line = file1.readline()

    if not line:
        break
    

    a  = line.split('-')[0].strip('\n')
    b = line.split('-')[1].strip('\n')
    graph[a].append(b)
    graph[b].append(a)


file1.close()

print(traverse('start', {'start'}, False))
print(traverse('start', {'start'}, True))