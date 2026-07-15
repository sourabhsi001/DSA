class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word=set(word)
        ans=0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in word and i.upper() in word:
                ans+=1
        
        return ans
        