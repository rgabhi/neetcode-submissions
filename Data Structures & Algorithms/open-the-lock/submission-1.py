class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        u = '0000'
        q = deque()
        turns = 0
        vis = set()
        deadends = set(deadends)
        if u in deadends:
            return -1
       
        def neighbors(curr):
            nbs = []
            for i in range(4):
                digit = int(curr[i])
                for move in (-1, 1):
                    new_digit = (digit + move)%10
                    nbs.append(curr[:i] + str(new_digit) + curr[i+1:])
            return nbs
                

        q.append(u)
        while q:
            l = len(q)
            while l > 0:
                u = q.popleft()
                vis.add(u)
                if u == target:
                    return turns
                # print(combs)
                for v in neighbors(u):
                    if v not in vis and v not in deadends:
                        q.append(v)
                        vis.add(v)
                l -= 1
            turns += 1
        return -1





        