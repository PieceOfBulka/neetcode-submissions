class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        s = s.replace(' ','')
        for sign in string.punctuation:
            s = s.replace(sign, '')
        s = s.lower()

        left,right=0,len(s)-1
        while left<right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True