class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # out = []
        # for num in nums:
        #     val = num**2
        #     out.append(val)
        # return sorted(out)

        from collections import deque 
        answer = deque()
        l, r = 0, len(nums) - 1
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.appendleft(left*left)
                l += 1
            else:
                answer.appendleft(right*right)
                r -= 1
        return list(answer)