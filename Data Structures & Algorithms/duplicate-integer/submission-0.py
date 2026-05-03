class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct={}
        for el in nums:
            if el in dct:
                return True
            dct[el]=True
        return False        