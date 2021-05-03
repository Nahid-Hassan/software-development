class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        
        res = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[res]:
                res += 1
                nums[res] = nums[i]

        return res + 1