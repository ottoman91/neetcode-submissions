# create a hashmap -> number : frequency
# select all values where frequency == k

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        count = {}
        freq = [[] for i in range(len(nums) + 1)] 

        for num in nums:
            count[num] = 1 + count.get(num, 0) 
        for number, count in count.items():
            freq[count].append(number) 
        
        result = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                result.append(n) 
                if len(result) == k:
                    return result
