# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        #Method 1: use heap
        maxi = 0
        heap = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            start = interval.start
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            maxi = max(maxi, len(heap))
        return maxi

        #Method 2: sort twice
        maxi = 0
        i = 0
        cur = 0
        n = len(intervals)
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)
        for end in ends:
            while i < n and starts[i] < end:
                cur += 1
                i += 1
            maxi = max(maxi, cur)
            cur -= 1
        return maxi
