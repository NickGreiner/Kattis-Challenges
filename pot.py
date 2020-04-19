import math

numberOfAddends = int(input())
numberList = list()
powerList = list()

outputX = 0

for x in range(0, numberOfAddends):
    inputNumberStr = input()
    powerList.append(int(inputNumberStr[-1]))
    numberList.append((int(inputNumberStr[:-1])))

for i in range(0, len(numberList)):
    outputX = outputX + pow(numberList[i], powerList[i])

print(outputX)
