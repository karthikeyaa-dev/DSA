def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []  # stores indices of the days

    for i in range(n):
        # Check if today's temp is warmer than the last stored temp
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day  # How many days we waited
        stack.append(i)  # Store current day's index

    return answer
