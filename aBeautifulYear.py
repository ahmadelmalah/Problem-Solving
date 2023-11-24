def isDistinct(year):
    year = str(year)
    return (year[0] != year[1] and year[0] != year[2] and year[0] != year[3] and year[1] != year[2] and year[1] != year[3] and year[2] != year[3])

year = int(input())
while True:
    year+=1
    if(isDistinct(year)):
       print (year)
       break
