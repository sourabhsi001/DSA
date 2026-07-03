class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr=[]
        if ch not in word:
            return word
        
        index=word.index(ch)

        return word[:index+1][::-1]+word[index+1:]
        