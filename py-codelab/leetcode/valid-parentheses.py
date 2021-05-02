class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = list()
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) != 0:
                    p = stack.pop()
                    if (p == '(' and ch != ')') or (p == '{' and ch != '}') or (p == '[' and ch != ']'):
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False