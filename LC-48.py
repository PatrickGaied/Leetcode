class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # (x', y') = (n-1-y, x)
        # (x, y) = (y', n-x'-1)
        d = {}
        
        for x in range(n): # x'
            for y in range(n): # y'
                pre_im = (y, n-x-1) # (x, y)
                d[(x, y)] = matrix[pre_im[1]][pre_im[0]]

        for key in d:
            matrix[key[1]][key[0]] = d[key]