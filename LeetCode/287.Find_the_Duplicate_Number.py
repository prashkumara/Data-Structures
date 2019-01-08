def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    fast = 0
    while slow != fast:
        fast = nums[fast]
        slow = nums[slow]
    return slow