class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        count=0
        fre={
            'a':0,
            'b':0,
            'c':0
        }
        for i in range(len(s)):
            fre[s[i]]+=1
            while fre['a']>0  and fre['b']>0 and fre['c']>0:
                count +=len(s)-i
                fre[s[left]] -=1
                left +=1
        return count