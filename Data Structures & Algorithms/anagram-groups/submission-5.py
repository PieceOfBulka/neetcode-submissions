class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for word in strs:
            dct=[0]*26
            for sign in word:
                dct[ord(sign)-ord('a')] += 1
            dct=tuple(dct)
            if dct not in res:
                res[dct]=[]
            res[dct].append(word)
        return list(res.values())