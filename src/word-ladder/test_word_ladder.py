import word_ladder as ladder
import pytest


def assert_valid_sequence(seq):
    for left, right in zip(seq[0:-1], seq[1:]):
        differences = ladder.count_differences(left, right)
        assert differences == 1


def test_one_step():
    sol = ladder.solve('aah', 'aal')
    assert_valid_sequence(sol)
    assert len(sol) == 2
    assert sol[0] == 'aah'
    assert sol[-1] == 'aal'


def test_tricky_1():
    sol = ladder.solve('all', 'all')
    assert len(sol) == 1
    assert sol[0] == 'all'


def test_tricky_2():
    sol = ladder.solve('AIL', 'ALL')
    assert_valid_sequence(sol)
    assert len(sol) == 2
    assert sol[0].lower() == 'ail'
    assert sol[-1].lower() == 'all'


def test_tricky_3():
    # Additional challenge: return an empty list if there is no solution
    # (easy version)
    sol = ladder.solve('gnu', 'ism')
    assert_valid_sequence(sol)
    assert len(sol) == 0


def test_several_steps():
    sol = ladder.solve('cat', 'dog')
    assert_valid_sequence(sol)
    assert len(sol) >= 4
    assert sol[0] == 'cat'
    assert sol[-1] == 'dog'


# @pytest.mark.skip()
def test_challenge_1():
    # Additional challenge: return the shortest path
    sol = ladder.solve('cat', 'dog')
    assert_valid_sequence(sol)
    assert len(sol) == 4
    assert sol[0] == 'cat'
    assert sol[-1] == 'dog'


@pytest.mark.skip()
def test_challenge_2():
    # Additional challenge: this sequence is difficult to solve
    sol = ladder.solve('man', 'ape')
    assert_valid_sequence(sol)
    assert len(sol) == 6
    assert sol[0] == 'man'
    assert sol[-1] == 'ape'


@pytest.mark.skip()
def test_challenge_3():
    # Additional challenge: this sequence is extremely long
    # Solution: 'ghi','phi','pht','pit','ait','apt','ape','age','ago','ego'
    sol = ladder.solve('ghi', 'ego')
    assert len(sol) == 10
    assert sol[0] == 'ghi'
    assert sol[-1] == 'ego'


@pytest.mark.skip()
def test_challenge_4():
    # Additional challenge: return an empty list if there is no solution
    # (hard version).
    # Note: this is challenging because of the runtime and memory constraints
    # imposed by coderpad.
    sol = ladder.solve('ail', 'ism')
    assert len(sol) == 0


pytest.main()
