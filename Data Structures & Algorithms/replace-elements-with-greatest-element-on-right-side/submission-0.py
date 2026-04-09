class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_biggest = float('-inf')
        for i in range(len(arr) - 1, -1, -1):
            temp = current_biggest
            current_biggest = max(current_biggest, arr[i])
            arr[i] = temp
        arr[-1] = -1
        return arr