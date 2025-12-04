from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 3
    assert arrs.get([], 0, "test") == "test"

def test_get_out_of_range_index(self):
    assert arrs.get([1, 2, 3], 5) is None
    assert arrs.get([1, 2, 3], 10) is None

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_slice_start_greater_than_end(self):
    assert arrs.my_slice([1, 2, 3, 4, 5], 3, 2) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 4, 1) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 4, 1) == []