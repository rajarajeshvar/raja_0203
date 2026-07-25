class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=0
        n=list(str(n))
        
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if int(n[i])*int(n[j])>m:
                    m=int(n[i])*int(n[j])
                
        return m

