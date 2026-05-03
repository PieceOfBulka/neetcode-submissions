class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            dct={}
            for j in range(i+1, len(nums)):
                if nums[j] in dct:
                    res.add(tuple(sorted([nums[i], nums[j], dct[nums[j]]])))
                dct[-nums[i]-nums[j]] = nums[j]
        return [[el[0], el[1], el[2]] for el in res]