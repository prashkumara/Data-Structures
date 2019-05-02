import itertools
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        # print(self.array,random.shuffle(self.array))
        temp = random.sample(self.array, len(self.array))
        return temp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()