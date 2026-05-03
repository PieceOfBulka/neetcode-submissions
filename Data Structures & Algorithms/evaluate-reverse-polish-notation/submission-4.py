class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for el in tokens:
            if (el[0]=='-' and el[1:].isdigit()) or el.isdigit():
                stack.append(el)
            else:
                b=stack.pop()
                a=stack.pop()
                stack.append(str(int(eval(a+el+b))))
        return int(stack.pop())