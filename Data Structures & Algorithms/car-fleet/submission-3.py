from math import ceil
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_arr = sorted([(pos, speed[i]) for i, pos in enumerate(position)], key=lambda x: x[0])
        stack=[(target - sorted_arr[0][0]) / sorted_arr[0][1]]
        for i in range(1,len(sorted_arr)):
            times = (target-sorted_arr[i][0])/sorted_arr[i][1]
            while stack and stack[-1] <= times:
                stack.pop()
            stack.append(times)

        return len(stack)
