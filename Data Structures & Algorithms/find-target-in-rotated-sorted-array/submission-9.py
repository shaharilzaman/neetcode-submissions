class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        
        while l<= r:
            mid = (l+ r) //2
            if target == nums[mid]:
                return mid
            
            #case 1, the left is sorted and our target is either inside sorted or outside sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: #not within left sorted
                    l = mid + 1
                else: 
                    r = mid - 1
            
            #case 2, the r is sorted and our target is either inside sorted or outside sorted
            else:
                if target < nums[mid] or target > nums[r]: #not within r sorted
                    r = mid - 1
                else: 
                    l = mid + 1
        
        return -1