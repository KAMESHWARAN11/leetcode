class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s :
            if  ch in "({[" :
                stack.append(ch)
            elif not stack :
                return False
            elif stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return False
        return not stack