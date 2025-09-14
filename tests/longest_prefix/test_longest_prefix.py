import pytest

from src.longest_prefix.longest_prefix import Solution

class TestLongestPrefix:

    @pytest.mark.parametrize(
            "words, result", [
                (["flower", "float", "flying"], "fl"),
                (["car", "dogboat", "simple"], ""),
                (["ab", "a"], "a")
            ]
    )
    def test_solution(self, words, result):
        sol = Solution()
        output = sol.longestCommonPrefix(words)
        assert result == output
