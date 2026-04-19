# 1. for i in range(len(nums))
# 2. for j in range(i, len(nums)):
# 3. if nums[i] + nums[j] == target and i != j
# 4. output = [i,j]
# return output

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j] 
        return []
        