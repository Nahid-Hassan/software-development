#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start

import functools

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(x) for x in digits]
        num = int(''.join(s))
        num += 1
        return [int(x) for x in str(num)]

# @lc code=end

# Time Efficient Solution
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 1
        for i in range(len(digits)):
            flag, digits[-(i + 1)] = divmod(digits[-(i + 1)] + flag, 10)
        if flag == 1:
            return [1] + digits
        return digits
"""

# Memory Efficient Solution
"""
class Solution:
    def plusOne(self, digits):
        k=""
        for i in digits:
            k+=str(i)
        s=int(k)+1
        g=list(map(int,str(s)))
        return g  
"""