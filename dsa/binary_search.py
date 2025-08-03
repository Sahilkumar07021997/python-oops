def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    :param arr: List of sorted integers.
    :param target: Integer value to search for.
    :return: Index of target in arr if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
res_index = binary_search(arr, target)
print(f"Index of {target} in the array: {res_index}")
