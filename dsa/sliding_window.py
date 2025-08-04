# maximum sum subarray of size k using sliding window technique.
def max_sum_subarray(arr, k):
    """Find the maximum sum of a subarray of size k using sliding window technique."""
    n = len(arr)
    if n < k:
        return None  # Not enough elements for a subarray of size k

    max_sum = current_sum = sum(arr[:k])  # Initial sum of the first k elements
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]  # Slide the window
        max_sum = max(max_sum, current_sum)  # Update max sum if needed

    return max_sum


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    result = max_sum_subarray(arr, k)
    print(f"Maximum sum of subarray of size {k} is: {result}")
