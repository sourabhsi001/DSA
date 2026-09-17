class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:]=sorted(set(nums))
        
        print(nums)
        return len(nums)