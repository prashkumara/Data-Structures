class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sets = set()
        lis = []
        for i in nums:
            if i not in sets:
                sets.add(i)
            else:
                lis.append(i)
        return lis

