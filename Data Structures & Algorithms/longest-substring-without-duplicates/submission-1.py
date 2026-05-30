class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        dct={}
        l=r=0
        mx_len=0
        while r<len(s):
            if s[r] not in dct or dct[s[r]]<l:
                mx_len=max(mx_len,r-l+1)
            else:
                l=dct[s[r]]+1


            dct[s[r]] = r
            r+=1
        return mx_len