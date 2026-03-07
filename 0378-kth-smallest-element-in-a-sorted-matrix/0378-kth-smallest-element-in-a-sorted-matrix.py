class Solution(object):
    def kthSmallest(self, matrix, k):
        nums=[]
        for row in matrix:
            nums+=row
        return sorted(nums)[k-1]
        