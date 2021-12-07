#fifo stack
file1 = open('input.txt', 'r')

stack = [None,None,None]
temp_sum = None
increased = 0
while True:


    line = file1.readline()

    
    if not line:
        break

    stack.insert(0,int(line))
    stack.pop()

    if None not in stack:
        if temp_sum != None:
            if sum(stack) > temp_sum:
                increased +=1
        temp_sum=(sum(stack))



    
 
file1.close()
print(increased)