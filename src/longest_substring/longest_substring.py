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
            while s[index] in s[start:end] and start < end:
                if len(s[start:end]) > longest:
                    longest = len(s[start:end]) 
                start += 1
            if s[index] not in s[start:end]:
                end += 1
            index += 1
        if len(s[start:end]) > longest:
            longest = len(s[start:end])
        return longest
