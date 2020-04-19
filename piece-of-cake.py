# Nick Greiner
# https://github.com/NickGreiner

# Python 3.7

sideLength, horizontalCut, verticalCut = input().split()
sideLength = int(sideLength)

horizontalSide1 = int(verticalCut)
verticalSide1 = int(horizontalCut)
horizontalSide2 = sideLength - horizontalSide1
verticalSide2 = sideLength - verticalSide1

piecesVolume = list()

piecesVolume.append(horizontalSide1 * verticalSide1)
piecesVolume.append(horizontalSide1 * verticalSide2)
piecesVolume.append(horizontalSide2 * verticalSide1)
piecesVolume.append(horizontalSide2 * verticalSide2)

print(max(piecesVolume) * 4)
