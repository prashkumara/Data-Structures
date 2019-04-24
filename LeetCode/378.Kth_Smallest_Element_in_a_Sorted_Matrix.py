import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heap.append(matrix[i][j])

        heapq.heapify(heap)

        lis = heapq.nsmallest(k, heap)

        return lis[-1]