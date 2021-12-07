import pandas as pd


file1 = open('input.txt', 'r')

zeroes = [0,0,0,0,0,0,0,0,0,0,0,0]
ones = [0,0,0,0,0,0,0,0,0,0,0,0]
#zeroes = [0,0,0,0,0]
#ones = [0,0,0,0,0]
o2gnumbers = []
co2snumbers = []
while True:


    line = file1.readline()
    if not line:
        break

    o2gnumbers.append(list(line.strip('\n')))
    co2snumbers.append(list(line.strip('\n')))

    for idx, val in enumerate(line):
        if val != '\n':
            if int(val) == 0:
                zeroes[idx] += 1
            elif int(val) == 1:
                ones[idx] += 1
    
file1.close()

zip_object = zip(ones, zeroes)

gammabit = []
episilonbit = []
for element1, element2 in zip_object:
    if element1 > element2:
       gammabit.append('1')
       episilonbit.append('0')
    else:
        gammabit.append('0')
        episilonbit.append('1')

gammabit=''.join(gammabit)
episilonbit=''.join(episilonbit)

gammadec = int(gammabit, 2)
episilondec = int(episilonbit, 2)

print(gammadec * episilondec)

o2gnumbers = pd.DataFrame(o2gnumbers)


for idx, val in enumerate(gammabit):
    counts = o2gnumbers[idx].value_counts()
    if '0' in counts and '1' in counts:
        if int(counts['0']) > int(counts['1']):
            val = 0
        elif int(counts['1']) > int(counts['0']):
            val = 1
        elif int(counts['1']) == int(counts ['0']):
            val = 1
    elif '0' in counts and '1' not in counts:
        val = 0
    elif '0' not in counts and '1' in counts:
        val = 1
    o2gnumbers = o2gnumbers[o2gnumbers[idx] == str(val)]
    if o2gnumbers.shape[0] == 1:
        break
#o2dec = int(''.join(o2gnumbers.loc[2].tolist()),  2)

o2dec = int(''.join(o2gnumbers.loc[543].tolist()),  2)
print(o2dec)


co2snumbers = pd.DataFrame(co2snumbers)
for idx, val in enumerate(episilonbit):
    counts = co2snumbers[idx].value_counts()
    if '0' in counts and '1' in counts:
        if int(counts['0']) > int(counts['1']):
            val = 1
        elif int(counts['1']) > int(counts['0']):
            val = 0
        elif int(counts['1']) == int(counts ['0']):
            val = 0
    elif '0' in counts and '1' not in counts:
        val = 0
    elif '0' not in counts and '1' in counts:
        val = 1

    co2snumbers = co2snumbers[co2snumbers[idx] == str(val)]
    
    if co2snumbers.shape[0] == 1:
        #print(idx)
        #print(episilonbit)
        break

print(co2snumbers)
#co2dec = int(int(''.join(co2snumbers.loc[11].tolist()) , 2))
co2dec = int(int(''.join(co2snumbers.loc[324].tolist()) , 2))
print(o2dec)
print(co2dec)
print(o2dec * co2dec)