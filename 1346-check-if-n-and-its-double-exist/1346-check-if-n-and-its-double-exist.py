class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for i in arr:
            double = i * 2

            if i == 0:
                if arr.count(0) >= 2:
                    return True
            elif double in arr:
                return True

        return False