class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums=set(nums)
        arr=list(nums)
        arr.sort(reverse=True)
        ans=[]
        if len(arr)<k:
            return arr
        for i in range(k):
            ans.append(arr[i])

        return ans