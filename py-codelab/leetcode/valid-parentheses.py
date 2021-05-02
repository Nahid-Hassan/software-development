class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                p = stack.pop()
                if (ch == ')' and p != '(') or (ch == '}' and p != '{') or (ch == ']' and p != '['):
                    return False
        
        if len(stack) != 0:
            return False
        else:
            return True