class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort nums
        nums.sort()
        
        ### BRUTE FORCE SOLUTION ###
        # answer = 0
        # for i in range(1, len(nums)):
        # 	j, curr = i - 1, k
        # 	while j > -1 and curr >= nums[i] - nums[j]:
        # 		curr -= nums[i] - nums[j]
        # 		j -= 1
        # 	answer = max(answer, i - j)
        # return answer
        
        ### PREFIX SUM SOLUTION ###
        # create the object to be returned
        answer = 0
        # sort the numbers
        nums.sort()
        # set up the sliding window
        s = 0
        e = 0
        win_len = 0
        win_sum = 0
        # loop through nums
        while e < len(nums):
            win_sum += nums[e]
            win_len += 1
            while (nums[e] * win_len > win_sum + k):
                win_sum -= nums[s]
                win_len -= 1
                s += 1
            answer = max(answer, win_len)
            e += 1
        # return the solution
        return answer
