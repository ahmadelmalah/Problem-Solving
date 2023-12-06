def isConsistent(arr):
    num = arr[0]
    for i in arr:
        if i != num:
            return False
    return True

position = int(input().split()[1])
nums = input().split()
left_group = nums[0:position-1]
right_group = nums[position-1:]

if isConsistent(nums):
    print(0)
    exit() 

if isConsistent(right_group) == False:
    print(-1)
    exit()

consistent_item = right_group[0]
for i in reversed(range(len(left_group))): 
    if left_group[i] != consistent_item:
        print(i+1)
        exit()