class Solution(object):
    def kthSmallest(self, matrix, k):
        nums=[]
        for row in matrix:
            for num in row:
                nums.append(num)
        return sorted(nums)[k-1]
        