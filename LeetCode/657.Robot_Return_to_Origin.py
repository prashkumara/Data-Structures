def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    x, y = 0, 0

    for m in moves:
        if m == "R":
            y += 1
        if m == "L":
            y -= 1
        if m == "U":
            x -= 1
        if m == "D":
            x += 1
    if x == 0 and y == 0:
        return True
    else:
        return False