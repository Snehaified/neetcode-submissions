class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(0,len(strs[0])):
            record = 0
            for j in range(1,len(strs)):
                if i<len(strs[j]) and strs[0][i] == strs[j][i]:
                    record = record + 1
            if record + 1 == len(strs):
                lcp = lcp + strs[0][i]
            else:
                break
        return lcp            