class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) # pop from maxheap
            x = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, y - x)

        if len(stones) !=0:
            return -1*stones[0]
        else:
            return 0