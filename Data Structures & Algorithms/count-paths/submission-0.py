class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # intution: so i think first of all we could use some kind of recursion to go down either down or right and keep on doing that until we get to the bottom right corner using dfs mabye
        # this is kind of a hard problem to actually go through and do it manually to undersstand example 1. 
        # so we can mabye look at the basics or instructions and try to get something from that. we always have two options to either move right or down and once we reach the bottom right corner our loop or recursion or whatever should stop. 
        # to get the base case: we can mabye think about how many unique ways are there from the ending position to get to itself for every position - so the base case would be 1. 
        # then for the position to the left of the bottom right corner is also 1 because it can only move right to get to the bottom right corner and it cannot move down so it only has 1 way of reaching the bottom right corner. This is also the case for every box in the bottom row as it can only move to the right and not down. 
        # next, we can do this from the row above the bottom right corner and start from the first right-most position. This position can only move down 1 so it also is 1. the next one to the left of this (second right-most position on this row) it has has 2 ways it can go down one and right one to get to the bottom right corner, so it has a value of 2. and then as we go down the row each position's value increase by 1. 
        # now, for the top row you start with 1 again for the right most value as you cannot go right. But now, the next position to the left of this (second right-most position on this row) has 3 ways as you add the previous one from its row and take the value from position below it (2 + 1 = 3). The next position to its left, will have 6 (3 to its right + 3 below it). You will continue this until you reach the end of this row and get 21 as the output. 

        row = [1] * n

        for i in range(m - 1):
            newR = [1] * n
            for j in range(n - 2, -1, -1):
                newR[j] = newR[j + 1] + row[j]
            row = newR
        
        return row[0]
