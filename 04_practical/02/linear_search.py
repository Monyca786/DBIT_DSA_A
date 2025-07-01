def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

print(linear_search([40, 20, 30, 80], 30)) 
print(linear_search([4, 6, 9], 10))