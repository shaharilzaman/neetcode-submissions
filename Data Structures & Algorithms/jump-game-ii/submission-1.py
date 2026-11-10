class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        output = 0
        while l <= r and r < len(nums) - 1:
            currfar = 0
            for i in range(l, r + 1):
                currfar = max(currfar, i + nums[i])
            l = r + 1 
            r = currfar
            output += 1
        return output 