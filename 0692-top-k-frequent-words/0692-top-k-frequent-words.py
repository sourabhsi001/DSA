class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        fre={}
        ans=[]
        count=0
        for i in words:
            fre[i]=fre.get(i,0)+1
        
        sorted_words = sorted(fre, key=lambda x: (-fre[x], x))
        return sorted_words[:k]
        



        
