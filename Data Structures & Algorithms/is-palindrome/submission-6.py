class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        l = s.replace(' ','')
        for sign in string.punctuation:
            l = l.replace(sign, '')
        l = l.lower()
        return l == l[::-1]