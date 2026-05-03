class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l,r=1,10**9
        while l<r:
            mid=l+(r-l)//2
            res = sum([math.ceil(pile/mid) for pile in piles])
            if res>h:
                l=mid+1
            else:
                r=mid
        return l