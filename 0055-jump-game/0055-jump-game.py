# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n=len(nums)-1
#         i=0
#         while i<n:
#             if nums[i]==0 or nums[i]>n:
#                 return False
#             val=nums[i]
#             i+=val
            
#         return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        maxReach = 0

        while i < n:
            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

            if maxReach >= n - 1:
                return True

            i += 1

        return True 