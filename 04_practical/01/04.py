def sum_numbers(n, accumulator=0):
    if n == 0:
        return accumulator
    return sum_numbers(n - 1, accumulator + n)

print(sum_numbers(10))