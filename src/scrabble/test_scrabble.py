import pytest
from scrabble import solve, score

wordfile = "collins_scrabble_words-2019.txt"


def is_valid_sol(sol: dict, rack: str) -> bool:
    from collections import Counter
    if len(sol) == 0:
        return True
    tiles = Counter(rack)
    for key in sol:
        for word in sol[key]:
            if len(word) != key:
                return False
            wordc = Counter(word)
            if wordc - tiles != Counter():
                return False
    return True


class TestScrabble:
    def test_seven_tiles_one_sol(self):
        rack = "AAAAAAA"
        sol = solve(rack, wordfile)
        assert len(sol) == 1
        assert len(sol[2]) == 1
        assert sol[2][0] == "AA"
        assert is_valid_sol(sol, rack) is True

    def test_seven_tiles_no_sol(self):
        rack = "TTTTTTT"
        sol = solve(rack, wordfile)
        assert len(sol) == 0
        assert is_valid_sol(sol, rack) is True

    def test_seven_tiles_reg_sol(self):
        rack = "ACDILPS"
        sol = solve(rack, wordfile)
        assert len(sol) == 5
        assert is_valid_sol(sol, rack) is True

    def test_seven_tiles_double_char(self):
        rack = "TURTLES"
        sol = solve(rack, wordfile)
        assert len(sol) == 6
        assert is_valid_sol(sol, rack) is True

    def test_six_tiles(self):
        rack = "ABCDEF"
        sol = solve(rack, wordfile)
        assert len(sol) == 4
        assert is_valid_sol(sol, rack) is True

    def test_five_tiles(self):
        rack = "ABCDE"
        sol = solve(rack, wordfile)
        assert len(sol) == 3
        assert is_valid_sol(sol, rack) is True

    def test_four_tiles(self):
        rack = "ABCD"
        sol = solve(rack, wordfile)
        assert len(sol) == 2
        assert is_valid_sol(sol, rack) is True

    def test_three_tiles(self):
        rack = "ABC"
        sol = solve(rack, wordfile)
        assert len(sol) == 2
        assert is_valid_sol(sol, rack) is True

    def test_two_tiles(self):
        rack = "AB"
        sol = solve(rack, wordfile)
        assert len(sol) == 1
        assert is_valid_sol(sol, rack) is True

    def test_one_tile(self):
        rack = "A"
        sol = solve(rack, wordfile)
        assert len(sol) == 0
        assert is_valid_sol(sol, rack) is True


class TestScrabbleScore:
    def test_score_one_sol(self):
        rack = "AA"
        sol = solve(rack, wordfile)
        scr = score(sol)
        assert len(scr) == 1
        assert 'AA' in scr[2][0]

    def test_score_reg_sol(self):
        rack = "ABCDEFG"
        sol = solve(rack, wordfile)
        scr = score(sol)
        assert len(scr) == 10
        assert len(scr[11]) == 2
        assert "DECAF" in scr[11]
        assert "FACED" in scr[11]


pytest.main()
