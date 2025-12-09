class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            num=str(num)
            n=0
            for i in range(len(num)):
                n=n+int(num[i])
            num=n
        return num

        