class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re

        words = re.findall(r'\w+', paragraph.lower())

        fre = {}

        for word in words:
            if word not in banned:
                fre[word] = fre.get(word, 0) + 1

        return max(fre, key=fre.get)
            
            
        

        