# solution;
# for each position, we need product of prefixes and suffixes. 
# 1. create an array of results set at 1. 
# 2. set prefix initially at 1
# 3. iterate through each element, do result = prefix and then update prefix *= result[i]

# 4. set suffix at 1
# 5. iterate from the end of the list. 
# 5. result[i] = result [i] * suffix
# 6. suffix *= suffix * result[i]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        results = [1] * (len(nums))
       
        prefix = 1 
        for i in range(len(nums)):
            results[i] = prefix 
            prefix *= nums[i] 
        suffix = 1
        for i in range(len(nums) - 1, -1, -1): 
            results[i] = suffix * results[i] 
            suffix *= nums[i] 
        return results

        