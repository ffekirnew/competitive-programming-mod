class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = k * threshold
        # create the object to be returned
        answer = 0
        # set up the sliding window
        window = sum(arr[:k])
        for i in range(len(arr) - k + 1):
            answer += 1 if window >= threshold else 0
            window += arr[i + k] - arr[i] if i < len(arr) - k else 0
        # return the solution
        return answer
