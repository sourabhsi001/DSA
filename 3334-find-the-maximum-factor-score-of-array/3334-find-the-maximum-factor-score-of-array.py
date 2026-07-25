class Solution:
    def maxScore(self, nums: List[int]) -> int:

        max_score = math.gcd(*nums) * math.lcm(*nums)

        for i in range(len(nums)):

            arr = nums[:i] + nums[i+1:]

            if len(arr) == 1:
                score = arr[0] * arr[0]
            else:
                score = math.gcd(*arr) * math.lcm(*arr)

            max_score = max(max_score, score)

        return max_score