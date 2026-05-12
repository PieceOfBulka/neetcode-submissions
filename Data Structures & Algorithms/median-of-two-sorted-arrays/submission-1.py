class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n,m=len(nums1),len(nums2)
        l,r=0,n
        half=n+(m-n)//2
        while l<=r:
            x1=l+(r-l)//2
            x2=half-x1
            a_max=nums1[x1-1] if x1>0 else float('-inf')
            a_min=nums1[x1] if x1<n else float('inf')
            b_max=nums2[x2-1] if x2>0 else float('-inf')
            b_min=nums2[x2] if x2<m else float('inf')

            if a_max<=b_min and b_max<=a_min:
                if (n+m)%2!=0:
                    return min(a_min, b_min)
                else:
                    return (min(a_min, b_min) + max(a_max,b_max))/2
            elif a_max>b_min:
                r=x1-1
            else:
                l=x1+1