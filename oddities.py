# Nick Greiner
# https://github.com/NickGreiner

# Python 3.7

numberOfTests = int(input())

for x in range(0, numberOfTests):
    testInt = int(input())
    if abs(testInt) % 2:
        print(str(testInt) + " is odd")
    else:
        print(str(testInt) + " is even")
