class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x : x[0])
        prevInterval = intervals[0]
        cnt = 0
        for i in range(1, n):
            if intervals[i][0] >= prevInterval[1]:
                # no overlap
                #move to next
                prevInterval = intervals[i]
            else:
                # overlap
                # if interval i has smaller end,
                # less chance of overlap with further intervals
                if intervals[i][1] < prevInterval[1]:
                    prevInterval = intervals[i]
                # remove the other overlapping
                cnt += 1
        return cnt
        
        
