class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        monoincrease = True

        if A[0] > A[len(A) - 1]:
            monoincrease = False

        if monoincrease:
            for i in range(1, len(A)):
                if A[i - 1] > A[i]:
                    return False
        else:
            for i in range(1, len(A)):
                if A[i - 1] < A[i]:
                    return False
        return True
