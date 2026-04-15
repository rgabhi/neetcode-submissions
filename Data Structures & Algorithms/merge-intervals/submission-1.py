class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = [[intervals[0][0], intervals[0][1]]]
        for i in range(1, n):
            ls, le = ans[-1][0], ans[-1][1]
            cs, ce = intervals[i][0], intervals[i][1]

            if cs <= le:
                ans.pop()
                ans.append([min(ls, cs), max(le, ce)])
            else:
                ans.append([cs, ce])
        return ans
        