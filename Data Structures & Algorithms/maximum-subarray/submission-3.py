class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globmaz = nums[0]
        currmax = 0
        for i in range(len(nums)):
            if currmax < 0:
                currmax = 0
            currmax = currmax + nums[i]
            if currmax > globmaz:
                globmaz = currmax
        return globmaz