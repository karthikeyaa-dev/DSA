class Solution(object):
    def searchRange(self, nums, target):
        left=0
        right=len(nums)-1
        result=[-1,-1]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                start=mid
                end=mid
                while start>0 and nums[start-1]==target:
                    start-=1
                while end<len(nums)-1 and nums[end+1]==target:
                    end+=1
                
                result=[start, end]
                return result
            
            if nums[mid]<target:
                left=mid+1
            
            else:
                right=mid-1

        return result


        
