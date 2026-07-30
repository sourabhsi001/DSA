class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        arr=list(chain.from_iterable(grid))
        if len(arr)==1 and arr[0]<0:
            return 1
        
        arr.sort()
        ans=0
        for i in arr:
            if i<0:
                ans+=1
            if i==0 or i>0:
                return ans
            
        