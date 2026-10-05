class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        p1 = 0
        p2 = 0 
        for house in nums:
            output = max(p1 + house, p2)
            p1 = p2 
            p2 = output
        return output