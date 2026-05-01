# set initial current sum at 0. 
# set maximum_sum at the first value 
# iterate through each element in the list 
# 4. currentsum = current sum + n 
# if currentsum is negative, then discard it and set it again at zero
class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        max_array_sum = nums[0] 
        current_prefix_sum = 0  
        for num in nums:
            if current_prefix_sum < 0:
                current_prefix_sum = 0 
            current_prefix_sum += num 
            max_array_sum = max(max_array_sum, current_prefix_sum) 
        return max_array_sum
        