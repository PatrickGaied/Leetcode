import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # min heap, will keep track of the largest k elements
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
