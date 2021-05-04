#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = max(nums)

        if m < 1:
            return 1
        
        if len(nums) == 1:
            return 2 if nums[0] == 1 else 1
        
        nums = [x for x in nums if x > 0]

        res = 1
        for i in range(len(nums)):
            if res in nums:
                res += 1
            else:
                return res
        
        return res

# @lc code=end

