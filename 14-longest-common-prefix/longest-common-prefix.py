class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = min(len(s) for s in strs)
        prefix = ""

        for i in range(min_len):
            ch = strs[0][i]

            for s in strs:
                if s[i] != ch:
                    return prefix

            prefix += ch

        return prefix