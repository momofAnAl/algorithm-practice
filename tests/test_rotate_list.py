from rotate_list import rotate_list

def test_shift_by_is_less_than_list_length():
    list = ["a", "b", "c"] 
    shift_by = 1

    result = rotate_list(list, shift_by)

    assert result == ["c", "a", "b"]

def test_shift_by_is_equal_list_length():
    list = [1, "c", 11] 
    shift_by = 3

    result = rotate_list(list, shift_by)

    assert result == [1, "c", 11]

def test_shift_by_is_greater_than_list_length():
    list = [1, 2, 3, 4, 5]
    shift_by = 6

    result = rotate_list(list, shift_by)

    assert result == [3, 4, 5, 1, 2]
    
