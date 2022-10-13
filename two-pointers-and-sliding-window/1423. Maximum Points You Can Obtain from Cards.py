class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # set up the sliding window
        win_len = len(cardPoints) - k
        # create the object to be returned
        answer = sum(cardPoints) - sum(cardPoints[:win_len])
        curr = answer
        # loop through the cards
        l = 0
        r = win_len
        while r < len(cardPoints):
            curr += cardPoints[l] - cardPoints[r] 
            answer = max(answer, curr)
            l += 1
            r += 1
        # return the solution
        return answer
