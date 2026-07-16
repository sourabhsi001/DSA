import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        mx = nums[0]
        prefixGcd = []

        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(math.gcd(mx, x))

        prefixGcd.sort()

        i = 0
        j = n - 1
        ans = 0

        while i < j:
            ans += math.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans