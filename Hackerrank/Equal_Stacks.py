def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    sum_h1, sum_h2, sum_h3 = sum(h1), sum(h2), sum(h3)
    min_h = min(sum_h1, sum_h2, sum_h3)

    if min_h == 0:
        return 0

    matched = False
    while not matched:
        if sum_h1 > min_h:
            sum_h1 -= h1.pop(0)
        if sum_h2 > min_h:
            sum_h2 -= h2.pop(0)
        if sum_h3 > min_h:
            sum_h3 -= h3.pop(0)
        min_h = min(sum_h1, sum_h2, sum_h3)
        matched = (sum_h1 == sum_h2 == sum_h3)

    return min_h