class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range (len(nums)):
        #     for j in range (len(nums)):
        #         if nums[i] + nums[j] == target and i!= j:
        #             return [i, j]
        
        hashmap = {}

        for i in range(len(nums)):
            if (nums[i] not in hashmap):
                hashmap[nums[i]] = i
            
            needed = target - nums[i]

            if (needed in hashmap):
                if (hashmap[needed] != i):
                    return sorted([i, hashmap[needed]])
