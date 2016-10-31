f = open('sub_sum.txt')

N, S = list(map(int, f.readline().split()))

listOfNumber = list(map(int, f.readline().split()))

# listOfPartialSum
# -- making partial sum of list
def listOfPartialSum(li):
    result = []
    for i in range(len(li)):
        sliced = li[:i+1]
        result.append(sum(sliced))
    return result

listOfPSum = listOfPartialSum(listOfNumber)


def sub_sum(n, s, li):      # li에는 PartialSum이 된 list가 들어간다.
    ans = len(li)           # 몇개의 숫자를 더했는지를 알 수 있는 변수

    for i in range(len(li)):
        match = False
        val = li[i]

        if (val > s):
            targ = val - s
            l = 0
            r = i - 1

            while (l <= r):
                m = (l + r) // 2
                if (li[m] > targ):
                    r = m - 1
                elif (li[m] < targ):
                    l = m + 1
                else:
                    match = True
                    break

            if match:
                ans = min(i - m, ans)

            else:
                if (val - li[l] > s):
                    ans = min(i - l, ans)
                if (val - li[r] > s):
                    ans = min(i - r, ans)

        elif val == s:
            ans = min(i + 1, ans)
    if (ans == len(li)):
        ans = 0
    return ans

print(sub_sum(N, S, listOfPSum))
