class Solution(object):
    def topKFrequent(self, nums, k):
        nums = sorted(nums)
        num = list(set(nums))
        l1 = []
        l2 = []
        for i in num:
            l1.append(nums.count(i))
            l2.append(i)
        result = []
        for i in range(k):
            m = max(l1)
            j = l1.index(m)
            result.append(l2[j])
            l1.pop(j)
            l2.pop(j)
        return result


        