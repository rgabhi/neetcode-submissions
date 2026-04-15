"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n <= 1:
            return n
        min_days = 1
        intervals.sort(key=lambda x : x.start)
        pq = [intervals[0].end]
        for i in range(1, n):
            if intervals[i].start < pq[0]:
                #overlap
                heapq.heappush(pq, intervals[i].end)
                min_days += 1
            else:
                #empty earliest available room
                heapq.heappop(pq)
                # enter next meeting to that room
                heapq.heappush(pq, intervals[i].end)
        return min_days
            

