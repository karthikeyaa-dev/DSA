class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        max_water=0
        while left<right:
            res=(right-left)*min(height[left], height[right])
            max_water=max(max_water, res)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water
