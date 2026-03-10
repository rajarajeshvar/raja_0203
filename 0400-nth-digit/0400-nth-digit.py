class Solution(object):
    def findNthDigit(self, n):
        digit_length = 1
        count = 9
        start = 1

        
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Step 2: find the exact number
        num = start + (n - 1) // digit_length

        # Step 3: find the exact digit
        return int(str(num)[(n - 1) % digit_length])