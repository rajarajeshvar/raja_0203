class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        m=0
        for i in nums:
            for j in nums:
                if i>j:
                    m=m+1
            l.append(m)
            m=0  
        return l   