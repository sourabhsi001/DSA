class Solution(object):
    def hammingDistance(self, x, y):
 
        xor=x^y
        ans=bin(xor).count('1')
        return ans