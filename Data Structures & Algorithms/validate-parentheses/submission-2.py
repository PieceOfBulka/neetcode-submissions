class Solution:
    def isValid(self, s: str) -> bool:
        stack=[s[0]]
        for i in range(1,len(s)):
            if s[i]=='}':
                if not stack or stack.pop()!='{':
                    return False
            elif s[i]==')':
                if not stack or stack.pop()!='(':
                    return False
            elif s[i]==']':
                if not stack or stack.pop()!='[':
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        return True
