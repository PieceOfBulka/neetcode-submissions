class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[(temperatures[0],0)]
        res=[0]*len(temperatures)
        for i in range(1,len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                val, ind = stack.pop()
                res[ind]=i-ind
            stack.append((temperatures[i],i))
        
        return res
