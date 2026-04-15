class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        available = []
        pending = []
        for i in range(n):
            heapq.heappush(pending, (tasks[i][0], tasks[i][1], i))

        time = 0 
        ans= []
        while pending or available:
            while pending and pending[0][0] <= time:
                enqueueT, processT, idx = heapq.heappop(pending)
                heapq.heappush(available, (processT, idx))

            if not available:
                time = pending[0][0] 
                continue
           
            processT, idx = heapq.heappop(available)
            ans.append(idx)
            time += processT                   
        return ans
            
    

        