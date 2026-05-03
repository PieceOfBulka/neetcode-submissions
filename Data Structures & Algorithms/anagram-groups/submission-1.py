class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words=[]
        for word in strs:
            dct={}
            for sign in word:
                if sign not in dct:
                    dct[sign] = 0
                dct[sign] += 1
            words.append(dct)
        
        bins=[0]*len(strs)
        res=[]
        for i in range(len(strs)):
            if bins[i]==1:
                continue

            res.append([strs[i]])
            for j in range(i+1, len(strs)):
                if words[i] == words[j]:
                    bins[j]=1
                    res[-1].append(strs[j])
        return res