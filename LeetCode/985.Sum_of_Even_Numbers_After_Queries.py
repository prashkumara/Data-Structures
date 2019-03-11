class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total = 0
        for i in A:
            if i % 2 == 0:
                total += i

        res = []
        for q in queries:
            prev = A[q[1]]
            A[q[1]] += q[0]
            if prev % 2 == 0:
                total -= prev
            if A[q[1]] % 2 == 0:
                total += A[q[1]]
            res.append(total)
        return (res)