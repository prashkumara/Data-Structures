def pairs(k, arr):
    sets = set(arr)
    count = 0
    for a in (arr):
        if a - k in sets:
            count += 1

    return count