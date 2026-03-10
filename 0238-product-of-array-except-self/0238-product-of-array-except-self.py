class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=1
        h=0
        l=[]

        if nums.count(0)>1:
            return [0]*len(nums)
        if 0 in nums:
            for i in range(0,len(nums)):
                if nums[i]==0:
                    h=i
                else:
                    s*=nums[i]
                    l.append(0)
            print(h)
            l.insert(h,s)
            return l
        else:
            for i in nums:
                s*=i
            for i in nums:
                l.append(s/i)
            return l

        

            
        print(l)

