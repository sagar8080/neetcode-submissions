"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        endTime = intervals[0].end

        for interval in intervals[1:]:
            start_time = interval.start
            end_time = interval.end
            
            if start_time < endTime:
                return False
            elif start_time >= endTime:
                endTime = end_time
        
        return True
                
            
