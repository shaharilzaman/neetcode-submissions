class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        output = 0 
        currsum = 0 
        for i in nums:
            currsum += i
            diff = currsum - k 
            output += prefix.get(diff, 0)
            prefix[currsum] = 1 + prefix.get(currsum, 0)
        return output 