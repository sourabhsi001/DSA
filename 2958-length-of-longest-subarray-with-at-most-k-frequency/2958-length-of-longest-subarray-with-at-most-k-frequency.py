class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        fre = {}

        for i in range(len(nums)):
            fre[nums[i]] = fre.get(nums[i], 0) + 1

            while fre[nums[i]] > k:
                fre[nums[left]] -= 1
                left += 1

            ans = max(ans, i - left + 1)

        return ans