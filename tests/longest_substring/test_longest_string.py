""" Implementation of the medium difficulty problem 'find the longest substring' from leetcode."""
import pytest
from src.longest_substring.longest_substring import Solution

class TestLongestString:

    @pytest.mark.parametrize(
            "inputs, result", [
                ("abcabcbb", 3),
                ("pwwkew", 3),
                ("bbbbb", 1),
                (" ", 1),
                ("12345123", 5),
                ("dvdf", 3),
                ("aa", 1),
                ("ckilbkd", 5),
                ("ohvhjdml", 6)
            ]
    )
    def test_longest_string(self, inputs, result):
        soln = Solution()
        res = soln.lengthOfLongestSubstring(s=inputs)
        assert res == result
