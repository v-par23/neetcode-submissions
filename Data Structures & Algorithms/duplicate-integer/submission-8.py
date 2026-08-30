# class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:

    #     for i in range(len(nums)):
    #         for n in range(len(nums)):
    #             if (i == n): 
    #                 continue

    #             if (nums[i] == nums[n]):
    #                 return True
                
    #     return False


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

