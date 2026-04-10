class Solution:
    def calPoints(self, operations: List[str]) -> int:
        counter = []
        for operation in operations:
            if operation not in ['+', 'C', 'D']:
                counter.append(int(operation))
            if operation == "+":
                counter.append(counter[-1] + counter[-2])
            if operation == "D":
                    counter.append(counter[-1] * 2)
            if operation == "C":
                counter.pop(-1)

        return sum(counter)