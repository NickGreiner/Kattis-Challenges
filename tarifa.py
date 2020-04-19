mbTotal = int(input())
months = int(input())
usedPerMonth = list()

dataLeft = 0

for x in range(0, months):
    usedPerMonth.append(int(input()))

for i in range(0, len(usedPerMonth)):
    dataLeft = dataLeft + (mbTotal - usedPerMonth[i])

dataLeft = dataLeft + mbTotal

print(dataLeft)
