class Card :
    
    def __init__(self):
        self.set = {}
        self.collumnCount = [0,0,0,0,0]
        self.rowCount = [0,0,0,0,0]

    def addRow(self, row, rowIndex):
        for idx, val in enumerate(row):
            self.set[val] = [rowIndex,idx,0]

    def numcall(self,num):
        if num in self.set:
            self.rowCount[self.set[num][0]] += 1
            self.collumnCount[self.set[num][1]] += 1
            self.set[num][2]= 1

    
    def checkBingo(self):
        score = -1
        if 5 in self.rowCount:
            rowID = self.rowCount.index(5)
            winningnumbers = []
            for key, value in self.set.items():
                if value[0] == rowID:
                    winningnumbers.append(key)
            print(winningnumbers)
            score = 0
            for key, value in self.set.items():
                if value[2] == False:
                    score += key

        if 5 in self.collumnCount:
            colID = self.collumnCount.index(5)
            for key, value in self.set.items():
                if value[1] == colID:
                    winningnumbers.append(key)
            print(winningnumbers)
            score = 0
            for key, value in self.set.items():
                if value[2] == False:
                    score += key

        return score

    def __str__(self):
        #return str(self.set.keys())
        return str(self.set)

#use dictionaries

file1 = open('input.txt', 'r')

nums = file1.readline()

cardList = []
currentCard = None
row = 0
while True:

    line = file1.readline()

    if not line:
        cardList.append(currentCard)
        break
    
    if line == "\n":
        cardList.append(currentCard)
        row = 0
        currentCard = Card()
    else:
        line = list(map(int, line.split()))
        currentCard.addRow(line, row)
        row +=1
file1.close()
cardList.pop(0)

for i in cardList:
    print(i)

nums = list(map(int, nums.split(',')))



for i in nums:
    for card in cardList:
        card.numcall(i)

    for card in cardList:
        score = card.checkBingo()
        if score != -1:
            print(score*i)
            break
    else:
        continue
    break