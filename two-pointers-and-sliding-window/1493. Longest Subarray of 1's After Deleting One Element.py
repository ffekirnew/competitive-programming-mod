class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # create the object to be returned
        answer = 0
        # set up the sliding window
        l = 0
        r = 0
        deleted = 0
        # loop through nums
        while r < len(nums):
            if nums[r] == 0:
                deleted += 1
            while deleted == 2:
                if nums[l] == 0:
                    deleted -= 1
                l += 1
            answer = max(answer, r - l)
            r += 1
        # return the solution
        return answer
