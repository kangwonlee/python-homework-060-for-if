import pathlib
import random
import sys

import pytest


pytest_folder = pathlib.Path(__file__).parent.absolute()
proj_folder = pytest_folder.parent.absolute()

sys.path.insert(0, str(proj_folder))


import exercise


random.seed()

@pytest.fixture
def for_with_if() -> callable:
    if not hasattr(exercise, 'for_with_if'):
        found = []
        for name in dir(exercise):
            if callable(getattr(exercise, name)):
                found.append(getattr(exercise, name))
        assert 0 < len(found), f"Found no functions in exercise.py: {found}"
        assert len(found) == 1, f"Found more than one function in exercise.py: {found}"
        result = found[0]
    else:
        result = exercise.for_with_if
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


def test_for_with_if_odd(for_with_if,a, b, odd_sum):
    assert for_with_if(a, b, 1) == odd_sum


def test_for_with_if_even(for_with_if, a, b, even_sum):
    assert for_with_if(a, b, 0) == even_sum


if "__main__" == __name__:
    pytest.main([__file__])
