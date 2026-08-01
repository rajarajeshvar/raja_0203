class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        m=0
        l=[0]
        for i in range(len(gain)):
            l.append(l[i]+gain[i])

            if l[i+1]>=m:
                m=l[i+1]
        print(l)
        return m
        