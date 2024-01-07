from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.count += 1

        while self.queue[0] < t -3000:
            self.queue.popleft()
            self.count -= 1

        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)