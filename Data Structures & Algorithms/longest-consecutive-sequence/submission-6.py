class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        l, r = 0, 1
        res = 1
        while r < len(nums):
            if nums[r] == nums[r-1]:
                l += 1
                r += 1
            elif nums[r] == nums[r-1] + 1:
                r += 1
            else:
                l = r
                r += 1
            res = max(res, r - l)
        return res