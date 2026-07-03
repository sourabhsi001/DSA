class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr=[]
        if ch not in word:
            return word
        
        index=word.index(ch)

        for i in range(index+1):
            arr.append(word[i])
        
        ans=""

        while arr:
            ans += arr.pop()
        
        ans+= word[index+1:]
        return ans
        