class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()

        while n!=1:
            if n in seen:
                return False
            seen.add(n)

            ans=0
            for i in str(n):
                ans+=int(i)**2
            n=ans
        return True

        