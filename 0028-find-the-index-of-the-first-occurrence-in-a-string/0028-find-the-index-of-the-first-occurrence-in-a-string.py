class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            word=haystack[i:i+m]
            print(word)
            if word == needle:
                return i
        return -1
        