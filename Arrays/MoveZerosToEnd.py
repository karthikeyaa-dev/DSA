def move_zeros_to_end(arr):
    j = 0  # pointer for next non-zero placement

    # Move all non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1

    # Fill remaining positions with 0
    while j < len(arr):
        arr[j] = 0
        j += 1

    return arr

# Test
print(move_zeros_to_end([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
