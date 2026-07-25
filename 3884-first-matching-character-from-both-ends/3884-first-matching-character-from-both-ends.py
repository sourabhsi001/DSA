class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for i in range(len(s)):
            n=len(s)
            condition=n-i-1
            if s[i]==s[condition]:
                return i
        return -1

        