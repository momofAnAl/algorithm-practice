# AImagine a skyline of buildings and you were standing in front of them at ground level 0. How many of these buildings could you see?

# Given a list [-1, 1, 3, 7, 7, 3] determine which values could be "seen."

# The output should be: [1,3,7]

# Write your clarifying questions and implementation in skyline.py. To execute your code, run python3 skyline.py in the terminal.

def skyline(building_list):
    if not isinstance(building_list, list):
        return None
    
    seen_building = []
    tallest = 0
    
    i = 0
    while i < len(building_list):
        if not isinstance(building_list[i], int):
            building_list[i] = 0
        
        if building_list[i] > tallest:
            seen_building.append(building_list[i])
            tallest = building_list[i]
            
        i += 1
        
    return seen_building       
        
# print(skyline([-1, 1, 3, 7, 7, 3]))

assert skyline([-1, 1, 3, 7, 7, 3]) == [1,3,7]
assert skyline([]) == []
assert skyline([1, 1, 1, 1, 1, 1]) == [1]
assert skyline([-1, 2, 3, 2, 3, 3, 7, 8]) == [2, 3, 7, 8]
assert skyline([-1, -1, -3, -7, -7, -3]) == []
assert skyline([-1, -1, -3, "7", -7, -3]) == []