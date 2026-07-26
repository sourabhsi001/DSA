class Solution:
    def sortArrayByParity(self, nums):
        ans = []

        for num in nums:
            if num % 2 == 0:
                ans.append(num)

        for num in nums:
            if num % 2 == 1:
                ans.append(num)

        return ans