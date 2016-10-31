f = open('closest2point.txt')

N = int(f.readline())
li = []

for i in range(N):
    point = tuple(map(int, f.readline().split()))
    li.append(point)

li = sorted(li, key=lambda x: x[0])
li = sorted(li, key=lambda x: x[1])

def dist2Points(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def closest2Point(xP, yP):
    leng = len(xP)

    if (leng <= 3):
        min_value = dist2Points(xP[0], xP[1])
        closestPair = (xP[0], xP[1])
        for i in range(leng):
            for j in range(i + 1, leng):
                brute_dist = dist2Points(xP[i], xP[j])
                if brute_dist < min_value:
                    min_value = brute_dist
                    closestPair = (xP[i], xP[j])

        return (min_value, closestPair)
    else:
        xL = xP[:leng//2]
        xR = xP[leng//2:]
        xm = xP[leng//2][0]

        yL = [p for p in yP if p[0] <= xm]
        yR = [p for p in yP if p[0] > xm]

        (dL, pairL) = closest2Point(xL, yL)
        (dR, pairR) = closest2Point(xR, yR)

        (dmin, pairMin) = (dR, pairR)
        if dL < dR :
            (dmin, pairMin) = (dL, pairL)

        yS = [p for p in yP if abs(xm - p[0]) < dmin]
        nS = len(yS)

        (closest, closestPair) = (dmin, pairMin)

        for i in range(nS - 1):
            k = i + 1
            while k < nS and yS[k][1] - yS[i][1] < dmin:
                new_candidate = dist2Points(yS[k], yS[i])
                if new_candidate < closest:
                    (closest, closestPair) = (new_candidate, (yS[k], yS[i]))
                k += 1

        return (closest, closestPair)


print(closest2Point(li, li))


