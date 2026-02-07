class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr1=[]
        arr2=[]
        arr=[]
        for i in range(0,len(nums)):
            if i<len(nums)/2:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for i in range(len(arr1)):
            arr.append(arr1[i])
            arr.append(arr2[i])
        return arr
        