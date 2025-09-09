class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest, p1, p2 = 0, 0, len(height) - 1

        def d(i, j):
            return abs(i - j) * min(height[i], height[j])
        
        while p2 > p1:
            largest = max(d(p1, p2), largest) 
            
            if height[p1] == height[p2]:
                p1 += 1
                p2 -= 1
            elif height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
            
        return largest
