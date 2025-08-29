def product_list(lst):
    result = 1  # Bug fixed: start with 1
    for num in lst:
        result *= num
    return result

print(product_list([2, 3, 4]))
