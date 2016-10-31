def move(size, pos):
    isOut = False
    quarter = size // 4
    if size == 2:
        return [1]

    newPos = pos
    if not (3 * quarter >= pos > quarter):
        isOut = True
        if (pos > 3 * quarter):
            newPos = pos - 3 * quarter
    else:
        newPos = pos -  quarter

    print(newPos)
    outer = move(size // 2, newPos)
    transfer = [size // 2]
    inner = move(size // 2, newPos)
    outer = list(map(lambda x: x + size // 2, outer))
    if isOut:
        return outer + transfer + inner
    else:
        return inner + transfer + outer

print(move(16,15))

