# bineary search
# for each iteration, calculate hte middle value. if its higher than the target, then move l rightwards. if the 
# mid value is lesser than target, then move r pointer to right

# 1. initialize l and r pointers
# 2. while l<r, calcualte the mid point
# adjust the galues accordingly


class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        l, r = 0, len(nums) - 1
        while l <= r:
            m = ( l + r) // 2
            if nums[m] > target:
                r = m - 1 
            elif nums[m] < target:
                l = m + 1 
            else: 
                return m 
        return -1 
        