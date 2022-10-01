class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        distance_left_speed = [[target - position[i], speed[i]] for i in range(length)]
        distance_left_speed.sort(reverse=True)
        
        result = 0
        stack = []
        for i in range(length - 1, -1, -1):
            time = distance_left_speed[i][0] / distance_left_speed[i][1]
            
            while stack and time > stack[-1]:
                stack.pop()
            
            if stack == []:
                result += 1
            
            stack.append(time)
        
        return result
