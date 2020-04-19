numberOfCases = int(input())

for x in range(0, numberOfCases):
    testCase = input()

    revenueNotAdvertise, revenueAdvertise, costOfAdvertise = testCase.split()

    revenueNotAdvertise = int(revenueNotAdvertise)
    revenueAdvertise = int(revenueAdvertise)
    costOfAdvertise = int(costOfAdvertise)

    if revenueNotAdvertise < (revenueAdvertise - costOfAdvertise):
        print('advertise')

    elif revenueNotAdvertise > (revenueAdvertise - costOfAdvertise):
        print('do not advertise')

    elif revenueNotAdvertise == (revenueAdvertise - costOfAdvertise):
        print('does not matter')

    else:
        print('error')
