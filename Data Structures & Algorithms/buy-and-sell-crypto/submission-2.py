class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        l,r=0,1
        mx_profit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                mx_profit = max(prices[r] - prices[l], mx_profit)
            else:
                l=r
            r+=1
        return mx_profit