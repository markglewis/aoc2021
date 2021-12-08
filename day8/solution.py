def deduce(sequence):
    samples = {}
    cypher = {}
    for code in sequence[0].split(" ")+sequence[1].split(" "):
        code = code.strip('\n')
        if len(code) == 2:
            samples[1] = code
        elif len(code) == 4:
            samples[4] = code
        elif len(code) == 3:
            samples[7] = code
        elif len(code) == 7:
            samples[8] =code
        elif len(code) == 6:
            code = ''.join(sorted(code))
            if 690 not in samples:
                samples[690] = [code]
            else:
                if code not in samples[690]:
                    samples[690].append(code)
        elif len(code) == 5:
            code = ''.join(sorted(code))
            if 235 not in samples:
                samples[235] = [code]
            else:
                if code not in samples[235]:
                    samples[235].append(code)
                    
    

    cypher[list(set(samples[7]) - set(samples[1]))[0]] = 'a'
    cypher[samples[1]] = 'cf'
    print(samples)

    keys = [k for k, v in cypher.items() if v == 'cf'][0]
    for i in samples[690]:
        if keys[0] not in i:
            cypher[keys[0]] = 'c'
            cypher[keys[1]] = 'f' 
            samples[6] = i
        if keys[1] not in i:
            cypher[keys[0]] = 'f'
            cypher[keys[1]] = 'c'
            samples[6] = i

    

    for code in samples[235]:
        difference = ''.join(list(set(samples[6]) - set(code)))
        if len(difference) == 1:
            samples[5] = code
            cypher[difference] = 'e'

    for letter in ['a','b','c','d','e','f','g']:
        if letter not in samples[1]+samples[4]+samples[7]:
            if letter not in cypher:
                cypher[letter] = 'g'

    ckey = [k for k, v in cypher.items() if v == 'c'][0]
    ekey = [k for k, v in cypher.items() if v == 'e'][0]
    for code in samples[690]:
        if ckey in code and ekey in code:
            for letter in ['a','b','c','d','e','f','g']:
                if letter not in code:
                    cypher[letter] = 'd'

    for letter in ['a','b','c','d','e','f','g']:
        if letter not in cypher:
            cypher[letter] = 'b'

    return cypher

def decrypt(cypher, lineout):
    numberOutput = []
    for code in lineout[1].split():
        output = []
        for letter in code:
            output.append(cypher[letter])
        output = ''.join(sorted(output))

        if output == 'abcefg':
            numberOutput.append('0')
        elif output == 'cf':
            numberOutput.append('1')
        elif output == 'acdeg':
            numberOutput.append('2')
        elif output == 'acdfg':
            numberOutput.append('3')
        elif output == 'bcdf':
            numberOutput.append('4')
        elif output == 'abdfg':
            numberOutput.append('5')
        elif output == 'abdefg':
            numberOutput.append('6')
        elif output == 'acf':
            numberOutput.append('7')
        elif output == 'abcdefg':
            numberOutput.append('8')
        elif output == 'abcdfg':
            numberOutput.append('9')
    numberOutput = ''.join(numberOutput)
    

    return int(numberOutput)
    

file1 = open('input.txt', 'r')

sum = 0
while True:


    line = file1.readline()

    if not line:
        break

    line = line.split('|')

    cypher = deduce(line)

    outint = decrypt(cypher, line)
    sum += outint
    print(outint)
print(sum)
file1.close()