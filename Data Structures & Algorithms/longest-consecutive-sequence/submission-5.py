class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums2 = set(nums)
        for i in nums2:
            if (i - 1) not in nums2:
                count = 1
                while (i + count) in nums2:
                    count += 1
                longest = max(longest, count)
                
        return longest



