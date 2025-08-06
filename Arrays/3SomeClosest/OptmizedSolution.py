class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]
        l=len(nums)
        for i in range(l):
            left=i+1
            right=l-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if abs(s-target)<abs(closest-target):
                    closest=s
                elif s<target:
                    left+=1
                else:
                    right-=1
        return closest

