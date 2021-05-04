#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # res = []
        # if target in nums:
        #     res.append(bisect.bisect_left(nums, target))
        #     res.append(bisect.bisect_right(nums, target) - 1)
        # else:
        #     res.append(-1)
        #     res.append(-1)
        # return res

        if target not in nums:
            return [-1,-1]
        
        a = nums.index(target)
        b = nums.count(target)
        return [a, a+b-1]
# @lc code=end

