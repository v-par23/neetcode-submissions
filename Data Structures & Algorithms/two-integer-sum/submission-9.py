class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range (len(nums)):
        #     for j in range (len(nums)):
        #         if nums[i] + nums[j] == target and i!= j:
        #             return [i, j]

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            diff = target - nums[i]

            if diff in hashmap:
                if (hashmap[diff] != i):
                    return [hashmap[diff], i]
            
        return -1
