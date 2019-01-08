class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]

        for i in range(len(A[0])):
            lis=[]
            for j in range(len(A)):
                lis.append(A[j][i])
            res.append(lis)
        return (res)