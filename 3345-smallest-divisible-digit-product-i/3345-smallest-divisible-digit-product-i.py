class Solution:
    def smallestNumber(self, n,t):
        
        while True:
            prod=1
            x=str(n)
            for i in x:
                prod*=int(i)
            if prod%t==0:
                return n
            n+=1

            