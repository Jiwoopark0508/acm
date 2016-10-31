from functools import reduce
f = open('potion.txt')

def GCD(a, b):
    if (a % b == 0):
        return b
    else:
        return GCD(b, a % b)

# li1 for correct ratio, li2 for harry's ratio
def componentListCompare(li1, li2):
    leng = len(li1)
    for i in range(leng):
        if li1[i] < li2[i]:
            return False
    return True
# print result
def printResult(li1, li2):
    result = []
    leng = len(li1)
    for i in range(leng):
        result.append(li1[i] - li2[i])
    return result

testCase = int(f.readline())

for i in range(testCase):
    numOfPotion = int(f.readline())
    correctList = list(map(int, f.readline().split()))

    gcd = reduce(lambda x, y: GCD(x, y), correctList)
    relPList = list(map(lambda x: x // gcd, correctList))

    harryList = list(map(int, f.readline().split()))
    loopCount = 1
    while (not componentListCompare(correctList, harryList)):

        correctList = list(map(lambda x: x * loopCount, relPList))
        loopCount += 1

    spoonToAdd = printResult(correctList, harryList)
    print(' '.join(str(e) for e in spoonToAdd))




