class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = set()
        # nums.sort()
        # for i in range(1, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(temp))
        # return [list(i) for i in res]

        nums.sort()
        triplets = []



        for i, val in enumerate(nums):

            if (i > 0) and (val == nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                cSum = nums[l] + nums[r] + val
                if cSum > 0:
                    r -= 1
                elif cSum < 0:
                    l += 1
                else:
                    triplets.append([val, nums[l], nums[r]])
                    l += 1

                    while l < r and (nums[l] == nums[l - 1]):
                        l += 1
        return triplets
