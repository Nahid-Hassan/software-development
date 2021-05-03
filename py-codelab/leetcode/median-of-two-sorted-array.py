class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = list(sorted(nums1 + nums2))

        res_len = len(res)
        if res_len % 2 == 0:
            return (res[res_len // 2] + res[(res_len // 2) - 1]) / 2         
        else:
            return res[res_len // 2]
