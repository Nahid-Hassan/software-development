class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        strs.sort()

        mn = min(len(strs[0]), len(strs[-1]))

        res = ''
        for i in range(mn):
            if strs[0][i] == strs[-1][i]:
                res += strs[0][i]
            else:
                break
        return res