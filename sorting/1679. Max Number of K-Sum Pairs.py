class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # create the object to be returned
        answer = 0
        # sort the list
        nums.sort()
        # set up two pointers
        i = 0
        j = len(nums) - 1
        # loop through
        while i < j:
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                answer += 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        # return the solution
        return answer
