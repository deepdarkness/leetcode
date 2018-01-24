# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals

        intervals.sort(key=lambda a: a.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            now_node = intervals[i]
            if now_node.start > res[-1].end:
                res.append(now_node)
            else:
                res[-1].end = max(now_node.end, res[-1].end)

        return res
