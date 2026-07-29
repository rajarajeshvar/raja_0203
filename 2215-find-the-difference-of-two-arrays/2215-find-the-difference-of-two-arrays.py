class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        l1=[]
        set_a = set(nums1)
        set_b = set(nums2)
        l1.append(list(set_a - set_b))
        l1.append(list(set_b - set_a))  
        return l1