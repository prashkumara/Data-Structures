def isBalCheck(i, j):
    if i == "]" and j == "[":
        return "YES"
    if i == "}" and j == "{":
        return "YES"
    if i == ")" and j == "(":
        return "YES"
    return "NO"


def isBalanced(s):
    isBal = "YES"
    arraystack = []
    for i in s:
        if i in '[({':
            arraystack.append(i)

        if i in "]})":
            if len(arraystack) == 0:
                return "NO"
            isBal = isBalCheck(i, arraystack.pop())
            if isBal == "NO":
                return "NO"
    if len(arraystack) != 0:
        return "NO"
    return isBal