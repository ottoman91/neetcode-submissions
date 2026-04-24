# combination of 2 sum II solution. 
# 1. sort the numbers
# 2. iterate through each number.
# 3. if the number is the same as the previous number, skip. 
# 4. else for each number, create two pointers, left and right. 
# 5. l is at i + 1, r is at len() - 1
# 6. if the sum of three is greater than zero, reduce r by 1. if its more than zero, increase l by 1, else append it in the 


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue 
            left, right = index + 1, len(nums) - 1 
            while left < right:
                threeSum = number + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1 
                elif threeSum < 0:
                    left += 1 
                else: 
                    results.append([number, nums[left], nums[right]]) 
                    left+= 1  
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 
        return results
