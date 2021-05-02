class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
        while x > 0:
            rem = x % 10
            result = result * 10 + rem
            x = x // 10
        if not -2147483648< result <2147483647:
            return 0
        return sign*result
