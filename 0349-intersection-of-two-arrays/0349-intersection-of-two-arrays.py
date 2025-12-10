class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        l=[]
        
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                l.append(nums2[i])
        return l
            

