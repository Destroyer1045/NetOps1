#!/usr/bin/env python3

def test_passing():
    assert(10, 20, 30) == (10, 20, 30)


def test_failing():
    assert not(10, 20, 30) == (30, 20, 10)


# Not checked, does not prefix with test
def dummy_func():
    assert(1, 2, 3) == (1, 2, 3)
