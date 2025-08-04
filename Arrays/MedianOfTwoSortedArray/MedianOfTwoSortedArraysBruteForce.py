class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num=nums1+nums2
        num.sort()
        l=len(num)
        if l%2==0:
            n=l/2
            sum=num[n-1]+num[n]
            sum=sum/2.0
            return sum
        else:
            n=l//2
            return num[n]

        
        
