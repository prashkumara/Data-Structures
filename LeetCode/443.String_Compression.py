def compress(self, chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    op = ""
    key = 0
    value = 1
    for i in range(len(chars) - 1):
        if chars[i] == chars[i + 1]:
            value += 1
        else:
            op = op + (chars[i])
            if value > 1:
                op = op + (str(value))
            value = 1

    op = op + (chars[len(chars) - 1])
    if value > 1:
        op = op + (str(value))
    if len(op) <= len(chars):
        for i in range(len(op)):
            chars[i] = op[i]
        return (len(op))
    else:
        return len(chars)