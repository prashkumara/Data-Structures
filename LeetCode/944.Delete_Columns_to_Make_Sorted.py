class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        flag = False

        for i in range(len(A[0])):
            for j in range(len(A) - 1):

                if not flag:
                    if A[j][i] > A[j + 1][i]:
                        flag = True

            if flag:
                count += 1
                flag = False

        return count
