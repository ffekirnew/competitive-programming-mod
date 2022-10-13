class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort the list based on starting time
        trips.sort(key = lambda x: x[1])
        # create a hashmap and keep track of when seats will be free
        taken_seats = {}
        # traverse through trips
        length = 0
        curr_passengers = 0
        i = 0
        while length < trips[-1][2]:
            if length in taken_seats:
                curr_passengers -= taken_seats[length]
                del taken_seats[length]
            while i < len(trips) and trips[i][1] == length:
                if capacity - curr_passengers >= trips[i][0]:
                    taken_seats[trips[i][2]] = taken_seats.get(trips[i][2], 0) + trips[i][0]
                    curr_passengers += trips[i][0]
                    i += 1
                else:
                    return False
            length += 1
        return True
