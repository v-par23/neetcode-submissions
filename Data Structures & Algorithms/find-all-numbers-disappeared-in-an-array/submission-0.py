class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list = []
        for i in range(1, len(nums)+1):
            if i not in set(nums):
                list.append(i)
        return list