def quicksort(arr: list[int]) -> list[int]:
    """My implementation of quicksort, sorting in increasing order"""
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # Naive pivot selection

    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3, 6, 8, 10, 1, 2, 1]))
print(quicksort([3, 3, 6, 8, 10, 1, 2, 1]))
