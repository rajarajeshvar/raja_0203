class Solution(object):
    def search(self, nums, target):                                      
        l=0
        m=len(nums)-1
        if len(nums)==1:
            if target in nums:
                return 0
            else:
                return -1
        if target<nums[l]:
            while target!=nums[m]:
                m=m-1
                if m==l:
                    return -1
            return m
        else:
            while target!=nums[l]:
                l=l+1
                if target==nums[l]:
                    return l
                if l==m:
                    return -1
            return l
        


