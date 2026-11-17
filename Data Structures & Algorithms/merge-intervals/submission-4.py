class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = sorted(intervals, key=lambda x: x[0])
        output = [sort[0]]
        for i in sort[1:]:
            if i[0] in range(output[-1][0], output[-1][1]+1):
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output.append(i)
        return output