from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
                continue
            elif len(stack)%2 == 1 and stack[-1] <= num:    
                stack.pop() # current num is greater than even index num
            elif len(stack)%2 == 0 and stack[-1] >= num:    
                stack.pop() # current num is smaller than odd index num 
            stack.append(num)
            
        if len(stack)%2 == 0: stack.pop()   # remove odd index value
            
        res = 0
        for i in range(len(stack)):
            if i%2 == 0:
                res += stack[i]
            else:
                res -= stack[i]
        
        return res