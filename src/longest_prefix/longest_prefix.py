class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        seen = ""
        count = len(strs)
        word = strs[0]
        for idx, ch in enumerate(word):
            for other in range(1, count):
                if len(strs[other]) <= idx:
                    return seen
                if strs[other][idx] != ch:
                    return seen
            seen += ch
        return seen
