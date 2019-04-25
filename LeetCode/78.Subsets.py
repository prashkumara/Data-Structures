from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        for i in range(len(nums)+1):
            combination = list(combinations(nums,i))
            #print(list(combination))
            for comb in (combination):
                res.append(list(comb))

        return(res)