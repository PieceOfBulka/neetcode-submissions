class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        l,r=0,1
        mx_profit=0
        while l<=r and r<len(prices):
            mx_profit = max(prices[r] - prices[l], mx_profit)
            if prices[l]>prices[r]:
                l+=1
            else:
                r+=1
        return mx_profit