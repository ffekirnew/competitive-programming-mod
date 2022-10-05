class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort nums
        nums.sort()
        # create the object to be returned
        answer = float('inf')
        distance = float('inf')
        # do the three sum algorithm
        # use more space, and reserve time, avoid function calls to abs() to find difference
        n = len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == target: 
                    return curr
                elif curr > target: 
                    k -= 1
                    if (curr - target < distance):
                        answer, distance = curr, curr - target
                else: 
                    j += 1
                    if (target - curr < distance):
                        answer, distance = curr, target - curr
        # return the solution
        return answer
