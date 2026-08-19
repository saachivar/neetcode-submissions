class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numArray = []
        nums.sort()
        for i, num in enumerate(nums[0:len(nums)-2]):
            if i == 0 or nums[i] != nums[i-1]:
                target = num * -1
                hashmap = {}
                last_used_companion = None  # Tracks duplicates in the inner loop
                for num2 in nums[i+1:]:
                    companion = target - num2
                    
                    # 1. Check if the needed companion exists
                    # 2. Ensure it's not a duplicate of the last companion we used for this target
                    if companion in hashmap and companion != last_used_companion:
                        array = [num, companion, num2]  # Uses original 'num' directly
                        numArray.append(array)
                        last_used_companion = companion  # Update our tracker
                        
                    # Store the number we have seen, not the subtraction logic
                    hashmap[num2] = True
        return numArray


        