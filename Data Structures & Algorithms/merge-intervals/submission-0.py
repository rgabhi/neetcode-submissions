class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals.sort()
        merged_intervals = []
        curr_s, curr_e = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            s, e = intervals[i][0], intervals[i][1]
            if s <= curr_e:
                curr_s = min(s, curr_s)
                curr_e = max(e, curr_e)
            else:
                merged_intervals.append([curr_s, curr_e])
                curr_s, curr_e = s, e
        merged_intervals.append([curr_s, curr_e])
        return merged_intervals