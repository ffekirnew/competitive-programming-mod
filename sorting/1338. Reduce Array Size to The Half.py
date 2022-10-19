class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr) // 2
        # count the frequencies of the items in the list and sort it
        arr = list(Counter(arr).values())
        arr.sort()
        # create a pointer
        i = len(arr) - 1
        # loop through arr
        tot = 0
        while i > -1:
            tot += arr[i]
            if tot >= size:
                break
            i -= 1
        return len(arr) - i
