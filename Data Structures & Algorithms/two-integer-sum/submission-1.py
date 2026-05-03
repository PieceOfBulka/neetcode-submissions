class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted([(nums[i], i) for i in range(len(nums))])
        left, right = 0, len(nums)-1
        while left<right:
            if sorted_nums[left][0] + sorted_nums[right][0] == target:
                return [min(sorted_nums[left][1], sorted_nums[right][1]),
                        max(sorted_nums[left][1], sorted_nums[right][1])]
            elif sorted_nums[left][0] + sorted_nums[right][0] > target:
                right-=1
            else:
                left+=1
