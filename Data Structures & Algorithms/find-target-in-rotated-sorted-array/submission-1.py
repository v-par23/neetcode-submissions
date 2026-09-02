class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2
            val = nums[m]
            if val == target:
                return m
            elif nums[l] <= nums[m]: #sorted left side
                if nums[l] <= target < nums[m]: #shrink towards left
                    r = m - 1
                else: #shrink towards right
                    l = m + 1 
            else: #sorted right side
                if nums[r] >= target > nums[m]: #shrink towards right 
                    l = m + 1
                else: #shrink towards left
                    r = m - 1
        return - 1