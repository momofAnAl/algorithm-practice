# Will shift_by be less than the length of the list? 
#   The value could be less than/equal/greater than length of list
# What if shift_by is a value not in the list? 
#   Still rotate the list by shift_by if valid
# Are negative number allowed for rotation value? 
#   Only valid shift_by values will be greater than 1
# Will the list always contain integers? 
#   Not necessarily, but we should still be able to shift it
# What if the list is empty? 
#   Return the empty list
# What if shift_by is invalid input? 
#   Raise an error or return None

def rotate_list(num_list, shift_by):
    if not isinstance(num_list, list):
        return []
    if not isinstance(shift_by, int):
        return None
    
    shift_by = shift_by % len(num_list)
    for _ in range(0, shift_by):
        num_list = [num_list[-1]] + num_list[:-1]
    
    return num_list
    
# def rotate(num_list):
#     last_element = [num_list[-1]]
#     remain_list = num_list[:-1]
    
#     update_list = last_element + remain_list

#     return update_list
        
print(rotate_list([1, 2, 3, 4, 5], 29))
print(rotate_list([1, 2, 3, 4, 5], 6))
print(rotate_list([1, 2, 3, 4, 5], 5))
print(rotate_list([1, 2, 3, 4, 5], 4))
       
assert(rotate_list([1, 2, 3, 4, 5], 1)) == [4, 5, 1, 2, 3]
assert(rotate_list([1, 2, 3, 4, 5], 6)) == [5, 1, 2, 3, 4]
assert(rotate_list([1, 2, 3, 4, 5], 5)) == [1, 2, 3, 4, 5]
assert(rotate_list([1, 2, 3, 4, 5], 4)) == [2, 3, 4, 5, 1]
        
   