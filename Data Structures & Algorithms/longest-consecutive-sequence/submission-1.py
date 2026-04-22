# naive solution.
# 1. sort the array in ascending order
# 2. declare longest_sequence = 0 
# 3. loop through each element in the array for i in range(len(array) - 1):
# if array[i+1] - array[i] = 1: longest_sequence += 1

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int: 
#         sorted_array = nums.sort() 
#         longest_sequence = 0 
#         for i in range(len(nums) - 1):
#             if nums[i+1] - nums[i] == 1:
#                 longest_sequence += 1 
#         return longest_sequence + 1

# alternative solution
# iterate through each number, if number - 1 not in set: then start of length of set.
# if n + 1 is in set, then 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        longest_sequence = 0 
        NumbersSet = set(nums)

        for n in nums:
            if (n - 1) not in NumbersSet:
                length = 0 
                while (n + length) in NumbersSet:
                    length += 1 
                    longest_sequence = max(longest_sequence, length)   
        return longest_sequence


