class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num1 = sorted(nums1 + nums2)
        index = len(num1) // 2
        if len(num1) % 2 != 0:
            return (num1[index])

        return (num1[index] + num1[index - 1]) / 2.0