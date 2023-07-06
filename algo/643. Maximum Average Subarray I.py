class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)

        max_k_sum = pre_sum[k] - pre_sum[0]
        for i in range(1, len(nums) - k + 1):
            if (pre_sum[i+k] - pre_sum[i]) > max_k_sum:
                max_k_sum = pre_sum[i+k] - pre_sum[i]
        return max_k_sum / k