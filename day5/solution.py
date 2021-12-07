import re

class VentsCoordinates:
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.horizontal = y1 == y2
        self.vertical = x1 == x2

    def __str__(self) -> str:
        return str(self.x1) + "," + str(self.x2) + " " + str(self.y1) +  "," + str(self.y2)

    def getHorizontal(self):
        return self.horizontal
    
    def getVertical(self):
        return self.vertical

    def getCoordinates(self):
        return (self.x1,self.y1,self.x2,self.y2)


file1 = open('input.txt', 'r')
hydrothermalVents = []

while True:

    
    line = file1.readline()


    if not line:
        break
    
    nums = list(map(int, re.findall('[0-9]+', line)))

    hydrothermalVents.append(VentsCoordinates(nums[0],nums[1],nums[2],nums[3]))
file1.close()

coordinates = {}

for vent in hydrothermalVents:
    if vent.getHorizontal():
        #print(vent.getCoordinates())

        x1 = vent.getCoordinates()[0]
        y1 = vent.getCoordinates()[1]
        x2 = vent.getCoordinates()[2]

        if x2 < x1:
            x1, x2 = x2, x1

        for i in range(x1,x2+1):
            #print(str(i)+ "," + str(y1))
            if (i,y1) in coordinates.keys():
                coordinates[(i,y1)] = coordinates[(i,y1)] + 1
            else:
                coordinates[(i,y1)] = 1
    
    if vent.getVertical():
        #print(vent.getCoordinates())
        x1 = vent.getCoordinates()[0]
        y1 = vent.getCoordinates()[1]
        y2 = vent.getCoordinates()[3]

        if y2 < y1:
            y1, y2 = y2, y1
        
        for i in range(y1,y2+1):
            #print(str(x1)+ "," + str(i))
            if (x1,i) in coordinates.keys():
                coordinates[(x1,i)] = coordinates[(x1,i)] + 1
            else:
                coordinates[(x1,i)] = 1

    if not vent.getHorizontal() and not vent.getVertical():
        print("diagonal")
        xchange,  ychange = 0,0
        x1 = vent.getCoordinates()[0]
        y1 = vent.getCoordinates()[1]
        x2 = vent.getCoordinates()[2]
        y2 = vent.getCoordinates()[3]

        if x1 < x2 :
            xchange = 1
        else:
            xchange = -1
        
        if y1 < y2:
            ychange = 1
        else:
            ychange = -1

        if (x1,y1) in coordinates.keys():
                coordinates[(x1,y1)] = coordinates[(x1,y1)] + 1
        else:
            coordinates[(x1,y1)] = 1
        while y1 != y2:
            print(x1,y1)
            x1 += xchange
            y1 += ychange
            if (x1,y1) in coordinates.keys():
                coordinates[(x1,y1)] = coordinates[(x1,y1)] + 1
            else:
                coordinates[(x1,y1)] = 1
    
count = 0
for k, v in coordinates.items():
    if v >=2:
        #print(k,v)
        count += 1
print(count)