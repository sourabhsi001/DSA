class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)-1
        s=list(s)
        i=0
        j=n
        v=['a','A','I','i','o','O','u','U','E','e']
        while i<j:
            if s[i] in v and  s[j] in v:
                s[i], s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] in v and s[j] not in v:
                j-=1
            elif s[j] in v and s[i] not in v:
                i+=1
            else:
                i+=1
                j-=1
        return ''.join(s)
           