class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            #1 add first row/list of matrix
            res += (matrix.pop(0))

            #2 append last element of all lists in order
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            #3 add reverse of last row/list
            if matrix and matrix[0]:
                res += (matrix.pop()[::-1])

            #4 append first element of all rows/lists in reverse
            if matrix and matrix[0]:
                for row in reversed(matrix):
                    res.append(row.pop(0))
            
        return res
