import pytest
from app import bubble_sort


data_to_sort = [
    ([1,2,3,4,5,21,7,4],[1,2,3,4,4,5,7,21]),
    ([20,1,5,3,6,7,2,9],[1,2,3,5,6,7,9,20])
    ]

@pytest.mark.parametrize('lst, sorted', data_to_sort)
def test_bubble_sort(lst, sorted):

    assert bubble_sort(lst) == sorted

