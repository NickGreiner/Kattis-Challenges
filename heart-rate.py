# Nick Greiner
# https://github.com/NickGreiner

# Python 3.7

numberOfCases = int(input())

for x in range(0, numberOfCases):
    beats, seconds = input().split()
    beats = float(beats)
    seconds = float(seconds)

    bpm = (60 * beats) / seconds
    abpmMin = bpm - (60 / seconds)
    abpmMax = bpm + (60 / seconds)

    print("%.4f" % abpmMin + " %.4f" % bpm + " %.4f" % abpmMax)
