def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stackList = []
    for i in s:
        if i in "[{(":
            stackList.append(i)
        else:
            if len(stackList) == 0:
                return False
            is_valids = Solution.checkIsValid(i, stackList.pop())
            if is_valids == False:
                return is_valids

    if len(stackList) == 0:
        return True
    else:
        return False


def checkIsValid(p1, p2):
    if p1 == "]" and p2 == "[":
        return True
    elif p1 == "}" and p2 == "{":
        return True
    elif p1 == ")" and p2 == "(":
        return True
    else:
        return False