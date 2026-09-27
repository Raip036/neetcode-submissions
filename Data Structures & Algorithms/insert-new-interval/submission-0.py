class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0

        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        intervals.insert(i, newInterval)

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start <= last_end:
                merged[-1][1] = max(last_end, end)

            else:
                merged.append([start,end])

        return merged
            

