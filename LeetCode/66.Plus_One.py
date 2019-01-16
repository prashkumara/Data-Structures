class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ""
        op = []
        for d in digits:
            string = string + str(d)
        string = str(int(string) + 1)

        for i in range(len(string)):
            op.append(int(string[i]))

        return op

