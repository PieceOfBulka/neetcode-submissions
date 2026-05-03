class Solution:

    def encode(self, strs: List[str]) -> str:
        length=[]
        s=''
        for l in strs:
            length.append(str(len(l)))
            s+=l
        return '!' + ' '.join(length) + '!' + s

    def decode(self, s: str) -> List[str]:
        i=1
        while s[i]!='!':
            i+=1
        lengths=list(map(int, s[1:i].split()))

        res=[]
        curr=i+1
        for length in lengths:
            res.append(s[curr:curr+length])
            curr+=length

        return res