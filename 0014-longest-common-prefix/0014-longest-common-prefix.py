class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        if not strs:
            return output
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return output
            output += strs[0][i]
        return output