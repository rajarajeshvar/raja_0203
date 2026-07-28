class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l=[]
        m=max(candies)
        for i in candies:
            if (i+extraCandies)>=m:
                l.append(True)
            else:
                l.append(False)
        return l
        