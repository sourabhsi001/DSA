class Solution:
    def absDifference(self, nums, k):
        nums.sort()

        small = sum(nums[:k])
        large = sum(nums[-k:])

        return abs(large - small)