import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def d(point):
            return point[0]**2 + point[1]**2
        heap = [[d(point), point] for point in points]
        heapq.heapify(heap) # compares first elements of heap[i]
        lst = []

        while k > 0:
            lst.append(heapq.heappop(heap)[1])
            k -= 1
        return lst
# O(n + klogn) time, O(n) space
