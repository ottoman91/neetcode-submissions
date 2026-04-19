# solution:
# 1. create a set, and calculate the length of the set. if the length of the set is less than the length of the list, then return true, else false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:  
        return len(nums) > len(set(nums))
        