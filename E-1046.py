class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Heapify then while len(stones) > 1: 
        # remove max/ if new max == old max remove max again, else
        # modify it then bubble it down/ 
        self.nums = stones
        self.heapify()

        while len(self.nums) > 1:
            Max = self.remove_max()
            if self.nums[0] == Max:
                self.remove_max()
            else:
                self.nums[0] = Max - self.nums[0]
                self.bubble_down(0)

        return self.nums[0] if self.nums else 0

        
    def heapify(self) -> None:
        n = len(self.nums)
        for i in range(n//2 - 1, -1, -1):
            self.bubble_down(i)
    
    def remove_max(self) -> int:
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        Max = self.nums.pop()
        self.bubble_down(0)
        return Max

    def bubble_down(self, i):
        left_i, right_i, n = 2*i+1, 2*i+2, len(self.nums)
        largest = i 
        
        if left_i < n and self.nums[left_i] > self.nums[i]:
            largest = left_i
        if right_i < n and self.nums[right_i] > self.nums[largest]:
            largest = right_i

        if largest == i:
            return
        if largest == left_i:
            self.nums[i], self.nums[left_i] = self.nums[left_i], self.nums[i]
            return self.bubble_down(left_i)
        self.nums[i], self.nums[right_i] = self.nums[right_i], self.nums[i]
        return self.bubble_down(right_i) 