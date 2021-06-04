class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif not stack or (c, stack.pop()) not in ((')', '('), (']', '['), ('}', '{')):
                return False
            
        return not stack
