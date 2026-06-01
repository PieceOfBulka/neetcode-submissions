class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dct={}
        for sign in s1:
            if sign not in dct:
                dct[sign]=0
            dct[sign] += 1

        l=0
        null_nums=0
        for r in range(len(s2)):
            if s2[r] in dct and dct[s2[r]]>0:
                dct[s2[r]]-=1
                if dct[s2[r]]==0:
                    null_nums+=1
                    if null_nums==len(dct):
                        return True
            else:
                while s2[l] in dct and s2[l]!=s2[r] and l<=r:
                    dct[s2[l]]+=1
                    if dct[s2[l]]==1:
                        null_nums-=1
                    l+=1
                else:
                    l+=1
        return False