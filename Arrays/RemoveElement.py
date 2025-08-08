class Solution(object):
    def removeElement(self, nums, val):
        w=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            else:
                nums[w]=nums[i]
                w+=1     
        return w  
