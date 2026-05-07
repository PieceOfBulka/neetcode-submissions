class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r=0,n-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        r=n+l-1
        while l<=r:
            mid=l+(r-l)//2
            mid_n=mid%n
            if nums[mid_n]==target:
                return mid_n
            elif nums[mid_n]<target:
                l=mid+1
            else:
                r=mid-1
        return -1