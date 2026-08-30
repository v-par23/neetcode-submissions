class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for n in range(len(nums)):
                if (i == n): 
                    continue

                if (nums[i] == nums[n]):
                    return True
                
        return False

        