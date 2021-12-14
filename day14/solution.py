from collections import Counter

file1 = open('input.txt', 'r')

polymer = file1.readline().strip('\n')

lettercount = Counter(polymer)
count = Counter()
for idx in range(len(polymer[:-1])):
    count[polymer[idx:idx+2]] += 1


instructions = {}
while True:
    line = file1.readline().strip('\n')

    if not line:
        break
    

    line = line.split()
    instructions[line[0]] = line[2]
file1.close()
print(instructions)


for i in range(40):
    tempcount = Counter()
    for key in count:
        a = key[0]+ instructions[key]
        b = instructions[key] + key[1] 
        tempcount[a] += count[key]
        tempcount[b] += count[key]
        lettercount[instructions[key]] += count[key]
    count = tempcount
print(lettercount)

max = None
min = None
for key,value in lettercount.items():
    if max  == None:
        max = value
        min = value
    else:
        if max < value:
            max = value
        if min > value:
            min = value
print(max-min)
