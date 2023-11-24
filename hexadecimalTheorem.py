input = int(input())

if (input == 0):
    print("0 0 0")
    exit()

if (input == 1):
    print("0 0 1")
    exit()

if (input == 2):
    print("0 0 2")
    exit()

fibArray = [3, 2, 1, 1, 0]
while True:
    if fibArray[0] == input:
        print(str(fibArray[4]) + " " + str(fibArray[3]) + " " + str(fibArray[1]))
        exit()
    
    fibArray[4] = fibArray[3]
    fibArray[3] = fibArray[2]
    fibArray[2] = fibArray[1]
    fibArray[1] = fibArray[0]
    fibArray[0] = fibArray[1] + fibArray[2]