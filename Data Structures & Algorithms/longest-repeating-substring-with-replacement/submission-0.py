class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len=0
        l=0
        dct={}
        for r in range(len(s)):
            if s[r] not in dct:
                dct[s[r]]=0
            dct[s[r]]+=1

            while (r-l+1)-max(dct.values())>k:
                dct[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)

        return max_len