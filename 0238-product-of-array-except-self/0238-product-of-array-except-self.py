class Solution(object):
    def productExceptSelf(self, nums):
        total=1
        zero_count=0
        for num in nums:
            if num==0:
                zero_count+=1
            else:
                total*=num
        ans=[]
        for num in nums:
            if zero_count>1:
                ans.append(0)
            elif zero_count==1:
                if num==0:
                    ans.append(total)
                else:
                    ans.append(0)
            else:
                ans.append(total//num)
        return ans