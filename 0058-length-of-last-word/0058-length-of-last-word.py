class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=s.split()
        word=arr[len(arr)-1]
        return len(word)
        