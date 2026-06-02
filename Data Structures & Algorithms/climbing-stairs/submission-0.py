class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[1,1]
        for i in range(n-1):
            dp.append(dp[-2]+dp[-1])
        return dp[-1]