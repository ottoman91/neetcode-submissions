# 1. sort the array of intervals by their first element first
# 2. traverse through each interval. if the start valye us less than the previous interval'
# end value, then merge the intervals. 
# 3 . otherwise, append

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals.sort(key = lambda x: x[0]) 
        results = [intervals[0]]
        for start_value, end_value in intervals[1:]:   
            last_value = results[-1][1]
            if start_value <= last_value:
                results[-1][1] = max(last_value, end_value) 
            else:
                results.append([start_value, end_value])
        return results
        
