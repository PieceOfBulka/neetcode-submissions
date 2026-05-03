class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_mult = 1
        has_one_zero = False
        has_two_zeros = False
        for el in nums:
            if el != 0:
                non_zero_mult *= el
            else:
                if has_one_zero:
                    has_two_zeros = True
                else:
                    has_one_zero = True

        res = []
        for el in nums:
            if el==0:
                if has_two_zeros:
                    res.append(0)
                else:
                    res.append(non_zero_mult)
            else:
                if has_one_zero:
                    res.append(0)
                else:
                    res.append(non_zero_mult//el)

        return res
