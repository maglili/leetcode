class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1 for _ in range(len(nums))]

        # Prefix product
        p = nums[0]
        for i in range(1, len(nums)):
            ans[i] = p
            p *= nums[i]

        # Suffix product * Prefix product
        p = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            ans[i] *= p
            p *= nums[i]
        
        return ans
        