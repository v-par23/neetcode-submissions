class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] == i:
                continue
            else:
                return i
        return len(nums)

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#             for i in range (0, len(nums)):
#                 return sum(range(len(nums)+1)) - sum(nums)
