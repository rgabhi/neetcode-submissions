class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        i = 0
        while i < n:
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
                i += 1
            elif newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                ans = ans + intervals[i:]
                return ans
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                i += 1
        ans.append(newInterval)
        return ans


        