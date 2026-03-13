import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        
        def can_finish(t):
            total = 0
            for w in workerTimes:
                x = int((math.sqrt(1 + 8 * t / w) - 1) // 2)
                total += x
            return total >= mountainHeight
        
        left = 0
        right = 10**16
        
        while left < right:
            mid = (left + right) // 2
            
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left