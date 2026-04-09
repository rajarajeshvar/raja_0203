class Solution(object):
    def intersect(self, nums1, nums2):
        d, res = {}, []
        for x in nums1: d[x] = d.get(x, 0) + 1
        for x in nums2:
            if d.get(x, 0) > 0: 
                res.append(x)
                d[x] -= 1
        return res
        