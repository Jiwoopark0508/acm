f = open('two_solution.txt')

n = int(f.readline())

solList = f.readline().split()
solList = list(map(int, solList))
solList.sort()

ans = 1000000

for i in range(len(solList)):
    l = i + 1
    r = len(solList) - 1
    val = -solList[i]

    # binary search; m is going to be
    while (l <= r):
        m = (l + r) // 2
        if (solList[m] < val):
            l = m + 1
        elif (solList[m] > val):
            r = m - 1
        else:
            break


    if (solList[m] == val):
        ans = 0
        x = i
        y = m
    else:
        if (ans > abs(solList[m] + solList[i])):
            ans = abs(solList[m] + solList[i])
            x = i
            y = m
        if (m < n - 1 and ans > abs(solList[m + 1] + solList[i])):
            ans = abs(solList[m + 1] + solList[i])
            x = i
            y = m + 1
        if (m - 1 > i and ans > abs(solList[m - 1] + solList[i])):
            ans = abs(solList[m-1] + a[i])
            x = i
            y = m - 1

print(solList[x], solList[y])
