class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fst = strs[0]
        for i in range(len(fst)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or fst[i] != strs[j][i]:
                    return fst[:i]

        return fst