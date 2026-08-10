class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, value in enumerate(nums):
            if (target-value) in hash:
                return [hash[target-value], i]
            else:
                hash[value] = i
        return[0,1]

        