class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        uniqueTriplets = set()
        for i, num in enumerate(nums[0:len(nums)-2]):
            target = num * -1
            hashmap = {}
            for num2 in nums[i+1:]:
                if num2 in hashmap:
                    array = [-1*target, target-num2, num2]
                    array.sort()
                    uniqueTriplets.add(tuple(array))
                else:
                    hashmap[(target-num2)] = target-num2;
        return list(uniqueTriplets)


        