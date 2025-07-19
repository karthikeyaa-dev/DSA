from collections import defaultdict

def frequency_counter(arr):
    count = defaultdict(int)
    for num in arr:
        count[num] += 1
    return count