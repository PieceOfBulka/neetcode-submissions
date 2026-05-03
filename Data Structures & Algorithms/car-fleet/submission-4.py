class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(el, ind) for ind, el in enumerate(position)]
        arr.sort(key=lambda x: x[0])
        ans = 1
        res = [(target-arr[-1][0]) / speed[arr[-1][1]]]
        for i in range(len(arr)-2, -1, -1):
            tmp = (target-arr[i][0]) / speed[arr[i][1]]
            if tmp <= res[-1]:
                res.append(res[-1])
            else:
                res.append(tmp)
                ans+=1
        return ans