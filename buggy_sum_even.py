def sum_even(lst):
    """
    Return the sum of all even numbers from the given iterable.
    
    Parameters:
        lst (iterable of int): Iterable of integers (or numeric types that support `%` and addition).
    
    Returns:
        int: Sum of elements for which `x % 2 == 0`. Returns 0 if no even elements are present.
    """
    return sum(x for x in lst if x % 2 == 0)  # Bug fixed: sum only even numbers

print(sum_even([1, 2, 3, 4, 5, 6]))
