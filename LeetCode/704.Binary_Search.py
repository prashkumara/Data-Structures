def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    def binSearch(nums, left, right, target):
        if right >= left:
            mid = left + (right - left) // 2
            print(mid)
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return binSearch(nums, left, mid - 1, target)

            else:
                return binSearch(nums, mid + 1, right, target)

        else:
            return -1

    return binSearch(nums, 0, len(nums) - 1, target)