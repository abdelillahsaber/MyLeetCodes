class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        prefix = ""
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in range(1, n):
                if i >= len(strs[j]) or strs[j][i] != letter:
                    return prefix
            prefix += letter
        return prefix