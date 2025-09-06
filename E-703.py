class KthLargest:
    # the goal here is to maintain a MinHeap that only stores the k largest elements
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.heapify() # min heap
        self.k = k

        while len(nums) > k: # remove smallest until we're left with k elements
             self.remove_min()


    def add(self, val: int) -> int:
        self.insert(val)  
        if len(self.nums) > self.k: 
            self.remove_min() 
        return self.nums[0]


    def heapify(self) -> None:
        n = len(self.nums)
        for i in range(n//2 - 1, -1, -1):
            self.bubble_down(i)
    
    def bubble_down(self, i):
        left_i, right_i, n = 2*i+1, 2*i+2, len(self.nums)
        smallest = i 
        
        if left_i < n and self.nums[left_i] < self.nums[i]:
            smallest = left_i
        if right_i < n and self.nums[right_i] < self.nums[smallest]:
            smallest = right_i

        if smallest == i:
            return
        if smallest == left_i:
            self.nums[i], self.nums[left_i] = self.nums[left_i], self.nums[i]
            return self.bubble_down(left_i)
        self.nums[i], self.nums[right_i] = self.nums[right_i], self.nums[i]
        return self.bubble_down(right_i) 

    def remove_min (self) -> None:
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        self.nums.pop()
        self.bubble_down(0)

    def insert(self, val) -> None:
        self.nums.append(val)
        self.bubble_up_last()

    def bubble_up_last(self):
        def p(j):
            return (j-1)//2
        i = len(self.nums) - 1
        while i > 0 and self.nums[i] < self.nums[p(i)]:
            self.nums[i], self.nums[p(i)] = self.nums[p(i)], self.nums[i]
            i = p(i)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)