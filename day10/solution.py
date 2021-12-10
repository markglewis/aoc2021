file1 = open('input.txt', 'r')

closedmatch = {")":"(","}":"{","]":"[",">":"<"}

scores = {")":3,"]":57,"}":1197,">":25137}

comepletionscores = {"(":1,"[":2,"{":3,"<":4}

score = 0
completedscores = []
while True:


    line = file1.readline()

    if not line:
        break

    illegalscount = {")":0,"}":0,"]":0,">":0}
    illegalchar = False
    
    stack = []
    for bracket in line:
        if bracket in ['(','{','[','<']:
            stack.append(bracket)
        elif bracket in [')','}',']','>']:
            if stack:
                expected = stack.pop()
                if expected != closedmatch[bracket]:
                    illegalscount[bracket] = illegalscount[bracket] + 1
                    illegalchar = True
                    break
            else:
                print("empty error")
                break
    
    
    linescore = 0
    for key,value in illegalscount.items():
        linescore += value * scores[key]
    score += linescore

    if illegalchar == False:
        finishedString = []
        completedlinescore = 0
        while stack:
            leftover = stack.pop()
            completedlinescore = completedlinescore * 5 + comepletionscores[leftover]
        completedscores.append(completedlinescore)

completedscores.sort()
index = int((len(completedscores) - 1)/2) 

print(score)
print(completedscores[index])

    
file1.close()