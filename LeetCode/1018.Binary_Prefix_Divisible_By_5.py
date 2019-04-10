class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """

        res = []

        st = ''
        for i in range(len(A)):
            # print()

            st = st + str(A[i])
            if int(st, 2) % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res