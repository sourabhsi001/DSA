class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(str(n))<=3:
            return 0
        return (n-1000)+1
        
            

        

        