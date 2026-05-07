class Solution:
    def binary_search(self,l,r,target,nums):
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r=0,n-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        if target==nums[0]:
            return 0
        elif target>nums[0]:
            if l==0:
                return self.binary_search(1,n-1,target,nums)
            else:
                return self.binary_search(1, l-1,target,nums)
        else:
            return self.binary_search(l,n-1,target,nums)