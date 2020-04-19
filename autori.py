inputString = input()
outputString = str()

for x in inputString:
    if x.isupper():
        outputString = outputString + x

print(outputString)