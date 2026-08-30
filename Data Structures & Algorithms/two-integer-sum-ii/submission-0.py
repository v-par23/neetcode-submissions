class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range (len(numbers)):
        #     for j in range (i+1, len(numbers)):
        #         if (numbers[i] + numbers[j]) == target and numbers[i] < numbers[j]:
        #             return [i + 1, j+ 1]
        #         return []

        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r+ 1]
              