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

# Awesome Solution
# Best time
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(":")", "[":"]", "{":"}"}
        
        for char in s:
            
            if char in mapping:
                stack.append(char)
            
            elif not stack:
                return False
            
            else:
                open_bracket = stack.pop() 
                if char != mapping[open_bracket]:
                    return False
    
        
        return not stack
"""

# Best Memory use
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','[':']','{':'}'}
        temp=[]
        for i in s:
            if i in dic.keys():
                temp.append(i)
            elif temp and dic[temp[-1]] == i:
                temp.pop()
            else:
                return False
        return(len(temp) == 0)               
"""