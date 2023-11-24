def isGarland(line):
    nums = line.split()
    nums = [int(x) for x in nums]
    if (nums[0] > nums[1]+nums[2]+1 or nums[1] > nums[0]+nums[2]+1 or nums[2] > nums[0]+nums[1]+1):
        print("No")
    else:
        print("Yes")

numOfLines = int(input())
for i in range(numOfLines):
    var = input()
    isGarland(var)