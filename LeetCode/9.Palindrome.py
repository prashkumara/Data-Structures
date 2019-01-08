def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        # print ("false")
        return False
    x1 = str(x)[::-1]
    if str(x) == x1:
        # print("true")
        return True
    else:
        # print ("false")
        return False