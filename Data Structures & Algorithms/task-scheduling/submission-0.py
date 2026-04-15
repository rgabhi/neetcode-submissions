class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) -1

        freq = list(freq.values())
        heapq.heapify(freq)

        q = deque()
        time = 0

        while freq or q:
            time += 1
            if freq:
                cnt = 1 + heapq.heappop(freq) # pop and decrement count by 1
                if cnt:
                    q.append((cnt, time + n))

            while q and q[0][1] == time:
                heapq.heappush(freq, q.popleft()[0])
            
        return time
            

        
        