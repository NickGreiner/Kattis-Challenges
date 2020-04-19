l = int(input())
d = int(input())
x = int(input())

outputs = list()

for n in range(l, d + 1):
    nStr = str(n)
    nDigits = list(nStr)
    nDigitTotal = 0

    for j in range(0, len(nDigits)):
        nDigitTotal = nDigitTotal + int(nDigits[j])
    if nDigitTotal == x:
        outputs.append(n)
    else:
        n = n + 1

print(min(outputs))
print(max(outputs))