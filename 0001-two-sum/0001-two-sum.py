class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    ans.append(i)
                    ans.append(j)
                    return ans
        return ans