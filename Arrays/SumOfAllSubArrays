def SubArraySum(arr, n):
    result = 0
 
    # computing sum of subarray
    # using formula
    for i in range(0, n):
        result += (arr[i] * (i+1) * (n-i))
 
    # return all subarray sum
    return result
 
 
# Driver code
arr = [1, 2, 3]
n = len(arr)
print("Sum of SubArray : ",
      SubArraySum(arr, n))