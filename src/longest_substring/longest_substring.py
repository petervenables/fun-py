class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1
        index = 1
        length = len(s)
        longest = 0
        if length <= 1:
            return length
        while index < length:
            if s[index] == s[index-1]:
                if len(s[start:end+1]) > longest:
                    longest = len(s[start:end])
                start = index
                index += 1
                end = index
            if index - end >= 2:
                if len(s[start:end+1]) > longest:
                    longest = len(s[start:end])
                start = index-1
                end = index
            if index >= length:
                continue
            if s[start] == s[index]:
                start += 1
            if s[index] not in s[start:end+1]:
                end += 1
            if len(s[start:end+1]) > longest:
                longest = len(s[start:end+1])
            index += 1
        return longest
