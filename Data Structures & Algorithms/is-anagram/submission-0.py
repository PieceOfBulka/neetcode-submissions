class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct={}
        for sign in s:
            if sign not in dct:
                dct[sign]=0
            dct[sign]+=1
        cnt=0
        for sign in t:
            if sign not in dct:
                return False
            dct[sign]-=1
            if dct[sign]==0:
                cnt+=1
        return cnt==len(dct)