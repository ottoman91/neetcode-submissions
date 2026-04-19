# 1. for i in range(len(nums))
# 2. for j in range(i, len(nums)):
# 3. if nums[i] + nums[j] == target and i != j
# 4. output = [i,j]
# return output

# brute force(conceptual)
# time complexity: O(n^2)
# space complexity: O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]: 
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target and i != j:
#                     return [i,j] 
#         return []


# initialize an empty hashmap.
# iterate through each index and value in the list 
# for each value, calculate the differenc ebetwqeen target and value
# if that value is in the hashmap, then return [position, i]
# else add that to the hashmap map[value] = i
# {}
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        prevMap = {}
        for key, value in enumerate(nums):
            difference = target - value 
            if difference in prevMap:
                return [prevMap[difference], key]
            prevMap[value] = key



