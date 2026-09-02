class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r+l)//2
            if nums[m-1] > nums[m]:
                return nums[m]
            elif nums[l] <= nums[m] > nums[r]: #cliff on right side
                l = m + 1
            else: #cliff on left side
                r = m - 1
            
        return nums[l]