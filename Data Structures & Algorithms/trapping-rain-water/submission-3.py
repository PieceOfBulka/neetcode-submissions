class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        while l<len(height) and height[l]==0:
            l+=1
        
        res=0
        fl=False
        while l<len(height):
            r=l+1
            walls=0
            while r<len(height) and height[r]<height[l]:
                walls-=height[r]
                r+=1
            if r==len(height):
                fl=True
                break
            res += walls + min(height[l], height[r])*(r-l-1)
            l=r

        if not fl:
            return res

        r=len(height)-1
        while r>l:
            l2=r-1
            walls=0
            while l2>l and height[l2]<height[r]:
                walls-=height[l2]
                l2-=1
            res += walls + min(height[l2], height[r])*(r-l2-1)
            r=l2

        return res