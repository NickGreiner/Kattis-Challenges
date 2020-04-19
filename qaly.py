periodsOfQuality = int(input())
qaly = 0.000

for x in range(0, periodsOfQuality):
    quality, years = input().split()
    qaly = qaly + (float(quality) * float(years))

print("%.3f" % qaly)