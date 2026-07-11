class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        i = 0
        j = len(nums) - 1
        move = 0

        while i < j:

            while j >= 0 and nums[j] == 0:
                j -= 1

            if i >= j:
                break

            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                move += 1
                j -= 1

            i += 1

        return move