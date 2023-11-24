def isEven(num):
    return num % 2 == 0

numOfLines = int(input())
rotatable = False
c0 = 0
c1 = 0
for i in range(numOfLines):
    line = input()
    nums = line.split()
    nums = [int(i) for i in nums]
    if isEven(nums[0] + nums[1]) == False:
        rotatable = True
    
    c0+=nums[0]
    c1+=nums[1]

if (isEven(c0) and isEven(c1)):
    print("0")
    exit()

if numOfLines == 1 or isEven(c0+c1) == False:
    print("-1")
    exit()


if rotatable:
    print("1")
else:
    print("-1")