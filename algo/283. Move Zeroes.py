class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[p_zero] == 0:
                nums[i], nums[p_zero] = nums[p_zero], nums[i]
            if nums[p_zero] != 0:
                p_zero += 1
            print(nums)