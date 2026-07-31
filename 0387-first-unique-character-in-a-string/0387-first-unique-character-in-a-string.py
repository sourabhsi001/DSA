class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre={}
        for i in s:
            fre[i]=fre.get(i,0)+1
        key=""
        for j,i in fre.items():
            if i ==1:
                key=j
                break
        for i in range(len(s)):
            if s[i]==key:
                return i
        return -1
        
