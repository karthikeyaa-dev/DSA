class Solution(object):
    def threeSum(self, nums):
        l=len(nums)
        result=set()
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1, l):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet=tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        return [list(t) for t in result]



        
