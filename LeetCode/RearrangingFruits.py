def minCost(basket1, basket2):
    from collections import Counter

    n = len(basket1)
    combined = basket1 + basket2
    freq = Counter(combined)

    # Check if rearrangement is possible
    for val in freq:
        if freq[val] % 2 != 0:
            return -1

    # Calculate excess counts
    count1 = Counter(basket1)
    count2 = Counter(basket2)

    excess1 = []
    excess2 = []

    for val in freq:
        diff = count1[val] - count2[val]
        if diff > 0:
            # val appears diff more times in basket1, add diff//2 to excess1
            excess1.extend([val] * (diff // 2))
        elif diff < 0:
            # val appears -diff more times in basket2, add (-diff)//2 to excess2
            excess2.extend([val] * ((-diff) // 2))

    excess1.sort()
    excess2.sort(reverse=True)  # reverse for minimal cost pairing

    smallest = min(combined)
    cost = 0

    for a, b in zip(excess1, excess2):
        # cost of direct swap
        direct_cost = min(a, b)
        # cost of swapping using smallest fruit twice
        indirect_cost = 2 * smallest
        cost += min(direct_cost, indirect_cost)

    return cost

