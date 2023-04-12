class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # recurrence relation: mincost(n) = cost(n) + min(mincost(n-1), mincost(n-2))
        # base case:
        #   mincost(0) = cost(0)
        #   mincost(1) = cost(1)
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])