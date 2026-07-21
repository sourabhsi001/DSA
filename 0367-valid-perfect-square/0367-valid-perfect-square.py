class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=math.sqrt(num)
        return n==int(n)

        