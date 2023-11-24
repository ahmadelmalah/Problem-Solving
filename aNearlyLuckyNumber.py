def getNumOfLuckyNums(number):
    count = 0
    for digit in number:
        if (digit == '4' or digit == '7'):
            count+=1
    return count

def isLucky(number):
    number=str(number)
    for digit in number:
        if (digit != "4" and digit != "7"):
           return "NO"
    return "YES"

numOfLuckyNums = getNumOfLuckyNums(input())
print(isLucky(numOfLuckyNums))