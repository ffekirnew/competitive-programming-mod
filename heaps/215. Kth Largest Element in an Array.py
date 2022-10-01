class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create the object to be returned
        answer = None
        # add the nums in the array into a priority queue
        queue = []
        for i in nums:
            heappush(queue, -1 * i)
        # pop them off one by one 
        for j in range(k):
            answer = -1 * heappop(queue)
        # return the object
        return answer
