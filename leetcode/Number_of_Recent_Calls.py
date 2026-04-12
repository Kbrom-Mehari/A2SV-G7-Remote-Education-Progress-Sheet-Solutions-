from collections import deque
class RecentCounter:

    def __init__(self):
        self.requests = deque()
        
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and t - self.requests[0] > 3000:
            self.requests.popleft()
        return len(self.requests)
        
recentCounter = RecentCounter()
print(recentCounter.ping(t=1))
print(recentCounter.ping(t=100))
print(recentCounter.ping(t=3001))
print(recentCounter.ping(t=3002))


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)