import math

matchesOnFloor, width, height = input().split()
matchesOnFloor = int(matchesOnFloor)
width = int(width)
height = int(height)
diagLenth = math.sqrt(math.pow(width, 2) + math.pow(height, 2))

lengthOfMatch = list()

for x in range(0, matchesOnFloor):
    lengthOfMatch.append(int(input()))

for i in range(0, len(lengthOfMatch)):
    if lengthOfMatch[i] <= diagLenth:
        print("DA")
    else:
        print("NE")
