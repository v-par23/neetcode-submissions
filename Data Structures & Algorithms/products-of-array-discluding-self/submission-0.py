import math 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if nums.count(0) > 1:
        #     return [0] * len(nums)
        
        # product = math.prod(nums)
        # produt_without0 = 1

        # for i in nums:
        #     if i == 0:
        #         continue
        #     product_without0 *= i
        
        # out = []
        # for i in nums:
        #     if i == 0:
        #         out.append(product_without0)
        #     else:
        #         out.append(int(product/i))
        
        # return out

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, - 1, - 1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res 





            
