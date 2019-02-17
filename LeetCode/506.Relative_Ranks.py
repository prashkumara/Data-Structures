class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        snums = sorted(nums, reverse=True)
        hashmap = {}
        for i in xrange(len(snums)):
            if i == 0:
                hashmap[snums[i]] = 'Gold Medal'
            elif i == 1:
                hashmap[snums[i]] = 'Silver Medal'
            elif i == 2:
                hashmap[snums[i]] = 'Bronze Medal'
            else:
                hashmap[snums[i]] = str(i + 1)

        for num in nums:
            res.append(hashmap[num])

        return res