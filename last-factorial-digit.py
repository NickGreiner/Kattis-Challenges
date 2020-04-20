# Nick Greiner
# https://github.com/NickGreiner

# Python 3.7

import math

numberOfTests = int(input())

for x in range(0, numberOfTests):
    factorial = str(math.factorial(int(input())))
    print(factorial[-1])
