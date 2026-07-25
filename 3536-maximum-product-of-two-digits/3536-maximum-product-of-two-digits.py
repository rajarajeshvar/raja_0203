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

        
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i]*l[j]>m:
                    m=l[i]*l[j]
                
        return m

