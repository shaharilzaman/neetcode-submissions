class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i in intervals:
            if i[1] < newInterval[0]:
                output.append(i)
            elif i[0] > newInterval[1]:
                output.append(newInterval)
                newInterval = i
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        output.append(newInterval)
        return output
        
        