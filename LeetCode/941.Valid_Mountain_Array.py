class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False

        maxelement = max(A)

        index = A.index(maxelement)
        if index == len(A) - 1 or index == 0:
            return False
        for i in range(index - 1):
            if A[i] >= A[i + 1]:
                return False
        for i in range(index, len(A) - 1):
            if A[i] <= A[i + 1]:
                return False
        return True