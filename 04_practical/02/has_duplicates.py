def has_duplicates(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False

print(has_duplicates([2,4,8,7,2,8,4]))  
print(has_duplicates([4, 2, 3, 1]))