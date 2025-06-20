class RecentCounter:

    def __init__(self):
        # Store only timestamps within the window
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        # Remove old timestamps from the front
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        # The length of the queue is the pings in the window
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t

if __name__ == "__main__":
    from collections import deque

    # Example usage
    counter = RecentCounter()
    print(counter.ping(1))      # Output: 1
    print(counter.ping(100))    # Output: 2
    print(counter.ping(3001))   # Output: 3
    print(counter.ping(3002))   # Output: 3
    print(counter.ping(6000))   # Output: 1
