# Nick Greiner
# https://github.com/NickGreiner

# Python 3.7

left, right = input().split()
left = int(left)
right = int(right)

if left == right and not right == 0:
    print("Even " + str(right * 2))

elif left > right:
    print("Odd " + str(left * 2))

elif left < right:
    print("Odd " + str(right * 2))

else:
    print("Not a moose")
