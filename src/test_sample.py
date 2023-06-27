import pytest


def fuc(x):
    return x + 1


def test_answer():
    assert fuc(3) == 5


# The -q/--quiet flag keeps the output brief in this and following examples.
if __name__ == '__main__':
    pytest.main(['-q', '/test_sample.py'])
