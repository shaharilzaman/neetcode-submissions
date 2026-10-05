class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self.robhelper(nums[:-1]), self.robhelper(nums[1:]))
    
    def robhelper(self, nums):
        output = 0 
        h1 = 0 
        h2 = 0
        for i in nums:
            output = max(i + h1, h2)
            h1 = h2
            h2 = output
        return output