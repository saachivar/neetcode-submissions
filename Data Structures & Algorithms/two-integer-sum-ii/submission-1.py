class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = {}
        for i, value in enumerate(numbers):
            if target-value in n:
                return [(n[target-value]+1), (i+1)]
            else:
                n[value] = i
        return