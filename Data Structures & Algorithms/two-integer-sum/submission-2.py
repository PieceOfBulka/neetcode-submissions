class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={target - nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in dct:
                return [dct[nums[i]], i]
            dct[target - nums[i]] = i