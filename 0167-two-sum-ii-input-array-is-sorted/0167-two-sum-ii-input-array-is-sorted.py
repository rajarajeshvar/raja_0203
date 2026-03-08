class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        
        return [l + 1, r + 1]