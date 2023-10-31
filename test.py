import lib

lists = [[2, 5, 7, 7, 8, 2], [2, 5, 7, 10], [2, 7]]

def test_CountElements_positive():
    assert lib.count_elements(lists) == 2

def test_CountElements_negative():
    assert lib.count_elements(lists) == 0
