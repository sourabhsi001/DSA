class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = list(chain.from_iterable(matrix))
        flat.sort()
        return flat[k-1]



        