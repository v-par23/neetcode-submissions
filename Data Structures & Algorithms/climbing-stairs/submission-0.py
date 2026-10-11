class Solution:
    def climbStairs(self, n: int) -> int:
        #step 1: 
        #define the sub-problem - basically what w have to find and its the thing that keeps on changing 
        #llike to go throught the base cases first and account for those essy solutions so we dont deal with that duringt he recurssion
        #step 2:
        #finding the recurrence formula:
        # n stairs 
        # examples: if n = 3, way 1: 1 step 3 times, way 2: 1 step 1 time, then 2 step 1 time, way 3: 2 step 1 time, then 1 step 1 time
        #so base case we can do for n = 1 is 1, for n = 2 is also 1 and n = 0 is 0 
        #
        def topdown(n, memo = None):
            if memo is None:
                memo = {}
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            memo[n] = topdown(n - 1, memo) + topdown(n - 2, memo)
            return memo[n]

        return topdown(n)