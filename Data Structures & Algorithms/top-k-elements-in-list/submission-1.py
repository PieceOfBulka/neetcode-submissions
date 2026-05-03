class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]]=0
            dct[nums[i]]+=1

        res = sorted(list(dct.items()), key=lambda x: x[1])
        return [el[0] for el in res[-k:]]
