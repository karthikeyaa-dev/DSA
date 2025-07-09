 class Solution:
    def minDist(self, arr, n, x, y):
        res = 2**31
        ix = iy = -1
        
        for i in range(n):
            if arr[i] == x: ix = i
            if arr[i] == y: iy = i
            if ix != -1 and iy != -1: res = min(res, abs(ix - iy))
            
        return res if res != 2**31 else -
