class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 9:
            return num
        while num > 9:
            add = 0
            for n in str(num):
                add = add + int(n)

            num = add
        return num

