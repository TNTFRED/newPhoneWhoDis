def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                # Swap if the elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
arr = [5, 2, 9, 1, 7]
bubble_sort_descending(arr)
print(arr)