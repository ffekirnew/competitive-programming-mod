class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [-i for i in Counter(tasks).values()]
        heapify(tasks)
        time = 0
        queue = deque()
        while tasks or queue:
            if tasks and tasks[0] != 0:
                queue.append([(heappop(tasks) * -1) - 1, time + n])
            if queue and queue[0][1] == time:
                heappush(tasks, -1 * queue.popleft()[0])
            time += 1
        return time
