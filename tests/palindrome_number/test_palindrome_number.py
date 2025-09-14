import pytest

from src.palindrome_number.palindrome_number import Solution

class TestPalindromeNumber:

    @pytest.mark.parametrize(
            "number, result", [
                (1234, False),
                (1221, True),
                (0, True),
                (10, False),
                (101010101, True),
                (1010150101, False),
                (-121, False)
            ]
    )
    def test_solution(self, number: int, result: bool):
        s = Solution()
        assert s.isAltPalindrome(number) == result
