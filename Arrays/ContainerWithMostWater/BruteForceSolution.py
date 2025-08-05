class Solution(object):
    def maxArea(self, height):
       l=len(height)
       max_water=0
       for i in range(0,l):
            for j in range(i+1,l):
                res=(j-i)*min(height[i], height[j])
                max_water=max(max_water, res)
        
       return max_water
