

def reverse(s):

    result = ""
    head = s[0]
    s = s[1:]

    if (head != 'x'):
        return head

    leftUpper = reverse(s)
    s = s[len(leftUpper):]
    rightUpper = reverse(s)
    s = s[len(rightUpper):]
    leftLower = reverse(s)
    s = s[len(leftLower):]
    rightLower = reverse(s)

    result = leftLower + rightLower + leftUpper + rightUpper

    return 'x' + result

print(reverse("xxwwwbxwxwbbbwwxxxwwbbbwwwwbb"))
