class Solution(object):
    def moveZeroes(self, nums):
        non_zero_ptr = 0
        
        for current_ptr in range(len(nums)):
            if nums[current_ptr] != 0:
                
                nums[non_zero_ptr], nums[current_ptr] = nums[current_ptr], nums[non_zero_ptr]
                
                
                non_zero_ptr += 1