class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        
        m=0
        for i in str(n):
            l.append(int(i))
        l=sorted(l,reverse=True)
        m=l[0]*l[1]
            
        return m

