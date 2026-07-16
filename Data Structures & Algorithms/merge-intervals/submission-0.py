class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        merged = []
        active = 0
        start_time = None

        # convert intervals to events
        for start, end in intervals:
            events.append((start, +1))
            events.append((end, -1))
        
        # sort the events in order
        events.sort(key=lambda x: (x[0], -x[1]))

        # iterate thru events
        for time, typ in events:
            if typ == 1:
                if active == 0:
                    start_time = time
                active += 1
            else:
                active -= 1
                if active == 0:
                    end_time = time
                    merged.append([start_time, end_time])
                
        return merged