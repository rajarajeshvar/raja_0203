class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max=0
        m=0
        for i in range(0,len(arr)):
            if arr[i] > max:
                max=arr[i]
                m=i
        return m
        