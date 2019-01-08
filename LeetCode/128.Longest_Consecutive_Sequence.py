class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets = set()
        for i in nums:
            sets.add(i)

        globalLength = 0
        length = 1
        for i in nums:
            loop = True
            while loop:

                if i + 1 in sets:
                    length += 1
                    i += 1
                else:

                    loop = False
            globalLength = max(length, globalLength)
            length = 1
        return globalLength
