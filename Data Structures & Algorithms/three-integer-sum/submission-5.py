# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         nums.sort()
#         for i in range (len(nums)):
#             for j in range (i + 1, len(nums)):
#                 for k in range (j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         temp = [nums[i], nums[j], nums[k]]
#                         res.add(tuple(temp))
#         return [list(i) for i in res]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for ind, v in enumerate(nums):

            #if i is same as prev val: has already been evaluvated
            if (ind > 0) and (v == nums[ind - 1]):
                continue

            l = (ind + 1)
            r = (len(nums) - 1)

            while l < r:
                cSum = v + nums[l] + nums[r]
                if cSum < 0:
                    l += 1
                elif cSum > 0:
                    r -= 1
                else:
                    triplets.append([v, nums[l], nums[r]])
                    # triplets.add(tuple(temp))

                    l += 1

                    while (l < r) and  (nums[l] == nums[l - 1]):
                        l += 1

        return triplets
                