class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        output = 0 
        h1 = 0 
        h2 = 0
        for i in nums:
            output = max(i + h1, h2)
            h1 = h2
            h2 = output
        return output