class Solution:
    def search(self, nums: List[int], target: int) -> int:
        output = 0 
        for i in nums:
            if i != target:
                output += 1
            else:
                return output
        return -1