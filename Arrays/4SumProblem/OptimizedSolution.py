class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        l=len(nums)
        result=set()
        for i in range(l):
            for j in range(i+1,l):
                left=j+1
                right=l-1
                while left<right:
                    s=nums[i]+nums[j]+nums[left]+nums[right]
                    if s==target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left+=1
                        right-=1
                    elif s<target:
                        left+=1
                    else:
                        right-=1

        return [list(m) for m in result]      
