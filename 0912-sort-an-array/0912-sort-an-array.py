class Solution(object):
    def sortArray(self, nums):
        if len(nums) == 0:
            return nums
        
        min_val = min(nums)
        max_val = max(nums)

        bucket_count = len(nums)
        bucket_range = (max_val - min_val) // bucket_count + 1
        buckets = [[] for _ in range(bucket_count)]
        for num in nums:
            index = (num - min_val) // bucket_range
            buckets[index].append(num)
        result = []
        for bucket in buckets:
            bucket.sort()
            result.extend(bucket)

        return result