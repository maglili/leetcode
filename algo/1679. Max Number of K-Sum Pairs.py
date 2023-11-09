class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        import collections
        counter = collections.Counter(nums)

        op = 0
        for num in counter:
            op += min(counter[num], counter[k-num])
        return op//2
