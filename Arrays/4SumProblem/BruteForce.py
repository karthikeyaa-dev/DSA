class Solution(object):
    def fourSum(self, nums, target):
        l=len(nums)
        result=set()
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1, l):
                    for m in range(k+1,l):
                        if nums[i]+nums[j]+nums[k]+nums[m]==target:
                            fours=tuple(sorted([nums[i],nums[j],nums[k], nums[m]]))  
                            result.add(fours)
        return [list(m) for m in result]      
