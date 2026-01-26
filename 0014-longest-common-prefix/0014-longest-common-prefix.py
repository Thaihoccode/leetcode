class Solution(object):
    def longestCommonPrefix(self, strs):
        #MANG RONG
        if not strs:
            return ""

        #MANG CO KY TU
        prefix = strs[0]

        for i in range(len(prefix)):
            for s in strs:
                if i >= len(s) or s[i] != prefix[i]:
                    return prefix[:i]

        return prefix
        