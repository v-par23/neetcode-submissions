class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        
        while l < r:
            m = (l+r)//2 

            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[l] <= nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return nums[l]