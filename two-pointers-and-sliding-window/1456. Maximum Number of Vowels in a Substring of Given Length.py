class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # list all vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        # create the object to be returned
        curr = 0
        for j in range(k):
            if s[j] in vowels:
                curr += 1
        answer = curr
        # set up the sliding window
        l = 0
        r = k
        while r < len(s):
            if s[r] in vowels: curr += 1
            if s[l] in vowels: curr -= 1
            answer = max(answer, curr)
            l += 1
            r += 1
        # return answer
        return answer
