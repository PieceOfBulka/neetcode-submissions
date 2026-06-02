class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        preprev,prev=0,cost[0]
        for i in range(1,len(cost)):
            preprev,prev=prev,min(preprev,prev)+cost[i]
        return min(preprev,prev)