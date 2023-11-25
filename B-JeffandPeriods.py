input()
originalNums = input()
originalNums = originalNums.split()
originalNums = [int(x) for x in originalNums]

distances = [-1] * 100001
indices = [-1] * 100001
count = 0

for i, num in enumerate(originalNums):
    # Skip invalid numbers
    if (distances[num] == -2):
        continue
    # First Time
    elif (distances[num] == -1):
        distances[num] = 0
        indices[num] = i
        count+=1
    elif  (distances[num] == 0):
        distances[num] = i - indices[num]
        indices[num] = i
    elif (distances[num] > 0):
        newDist = i - indices[num]
        if (newDist != distances[num]):
            distances[num] = -2
            count-=1
        else:
            indices[num] = i

print(count)
for i in range(100001):
    if (distances[i] < 0):
        continue

    print(str(i) + " " + str(distances[i]))