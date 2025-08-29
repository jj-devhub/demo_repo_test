def bubble_sort(arr):
    n = len(arr)
    # Bug fixed: optimize for already sorted portions
    for i in range(n):
        swapped = False
        for j in range(n-1-i):  # Bug fixed: correct range to avoid redundant comparisons
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # Early termination if array is sorted
            break
    return arr

def linear_search(arr, target):
    # Bug fixed: handle empty array
    if not arr:
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Bug fixed: correct right boundary
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test the fixed functions
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {data}")
print(f"Bubble sorted: {bubble_sort(data.copy())}")
print(f"Linear search for 25: {linear_search(data, 25)}")
print(f"Binary search for 25: {binary_search(sorted(data), 25)}")
print(f"Linear search in empty array: {linear_search([], 5)}")
