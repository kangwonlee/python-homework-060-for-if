import pathlib
import random
import os
import sys

import pytest


pytest_folder = pathlib.Path(__file__).parent.absolute()
proj_folder = pytest_folder.parent.absolute()

sys.path.insert(0, str(proj_folder))


import ex05


random.seed()

@pytest.fixture
def func05() -> callable:
    if not hasattr(ex05, 'func05'):
        found = []
        for name in dir(ex05):
            if callable(getattr(ex05, name)):
                found.append(getattr(ex05, name))
        assert 0 < len(found), f"Found no functions in ex05.py: {found}"
        assert len(found) == 1, f"Found more than one function in ex05.py: {found}"
        result = found[0]
    else:
        result = ex05.func05
    return result


@pytest.fixture
def a() -> int:
    return random.randint(1, 5)


@pytest.fixture
def b() -> int:
    return random.randint(6, 10)


@pytest.fixture
def odd_sum(a, b) -> int:
    return sum(i for i in range(a, b) if ((i % 2) == 1))


@pytest.fixture
def even_sum(a, b) -> int:
    return sum(i for i in range(a, b) if ((i % 2) == 0))


def test_func05_odd(func05,a, b, odd_sum):
    assert func05(a, b, 1) == odd_sum


def test_func05_even(func05, a, b, even_sum):
    assert func05(a, b, 0) == even_sum


if "__main__" == __name__:
    pytest.main([__file__])
