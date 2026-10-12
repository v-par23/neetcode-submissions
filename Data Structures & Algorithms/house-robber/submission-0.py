class Solution:
    def rob(self, nums: List[int]) -> int:
        #step 1: 
        #define the sub-problem - this is the thing that makes recursion better - with this we are ablto break down the problem and for some parts in the problem where we solve already we store those answers so we dont have to call the function again - idea of memoziation 
        #like to go through the base cases first and account for those essy solutions so we dont deal with that duringt he recurssion
            #base cases: case 1: if len(nums) == 0, then we return 0, case 2: if len(nums) == 1, then we return nums[i], case 3: if len(nums) == 2, then we return max(nums[i], nums[i + 1])
        #step 2:
        #finding the recurrence formula:
        # n stairs 
        # examples: nums = [1,7,2,1,10,6,8,9]
        # check if nums[i]
        # since we have the otpion to rob every other house at most - we can look to see if nums[i] + nums[i + 1] < nums[i+2], we would then just use nums[i + 2] as the next house to rob.
        # Optimizing idea before coding it
        # we basically have two options to either rob or skip house - we cannot look at nums[i], nums[i + 1], and nums[i + 2] all together so thats why we have to use the max feature.
        # hence, we take the max of option 1 (robbing house by taking nums[i] and skip to the next house nums[i + 2]) versus option 2 (skipping current house and only looking at nums[i + 1]) 
        # base case can only have 1 option and we have to let the recursive code handle the rest - so base case is only: if i >= len(nums): return 0

            if not nums:
                return 0
          
            def top_down(i, memo = None):
                if memo is None:
                    memo = [-1] * len(nums)
            
                if i >= len(nums):
                    return 0
                
                if memo[i] != -1:
                    return memo[i]

                skip = top_down(i + 1, memo)
                steal = nums[i] + top_down(i + 2, memo)

                memo[i] = max(skip, steal)
                return memo[i]
            
            return top_down(0)





            
            

