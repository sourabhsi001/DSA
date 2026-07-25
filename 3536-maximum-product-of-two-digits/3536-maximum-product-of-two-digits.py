class Solution:
    def maxProduct(self, n: int) -> int:
        arr=list(map(int,str(n)))
        arr.sort()
        n=len(arr)
        max_product=arr[n-1]*arr[n-2]
        return max_product
            