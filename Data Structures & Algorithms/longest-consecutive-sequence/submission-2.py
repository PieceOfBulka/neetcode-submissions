class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct={}
        for el in nums:
            dct[el]=True
        
        starts={}
        for el in dct:
            if el-1 not in dct:
                starts[el]=True

        res=0
        for start in starts:
            curr=start+1
            while curr in dct:
                curr+=1
            res=max(res, curr-start)
        
        return res