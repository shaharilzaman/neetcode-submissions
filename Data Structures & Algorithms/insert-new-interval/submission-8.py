class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i in intervals:
            # Case 1: current interval ends before new one starts → no overlap
            if i[1] < newInterval[0]:
                output.append(i)
            # Case 2: current interval starts after new one ends → no overlap
            elif i[0] > newInterval[1]:
                output.append(newInterval)
                newInterval = i  # move the "window" to this one
            # Case 3: overlap → merge intervals
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])

        output.append(newInterval)
        return output