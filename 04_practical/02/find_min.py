def find_min(list):
    if len(list) == 0:
        return None
    min_value = list[0]
    for item in list[1:]:
        if item < min_value:
            min_value = item
    return min_value

print(find_min([100, 20, 45, 30]))  
print(find_min([]))