class Solution:
    def calPoints(self, num: list[str]) -> int:
        record = []

        for i in num:
            if i == "+":
                record.append(record[-1] + record[-2])
            elif i == "D":
                record.append(2 * record[-1])
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))

        return sum(record)