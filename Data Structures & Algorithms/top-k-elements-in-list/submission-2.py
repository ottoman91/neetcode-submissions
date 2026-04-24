# bucket sort
# final output: an array, length equal to the length of the input array, each index -> frequency, valuues in each index(array) -> elements with that frequency
# iterate backwards through the array, write all results in a result array, stop when k = length(result), output the values

# 1. create a hashmap. integer: frequency of occurence
# 2. create an empty array of arrays, maximum integer = length of nums. 
# 3. iterate through teh hashamap, map each frequency to the empty array and add the numbers there. 

# 4. ite

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        counts_hashmap = {}
        frequency_array = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counts_hashmap[num] = 1 + counts_hashmap.get(num, 0) 
        for number, frequency in counts_hashmap.items(): 
            frequency_array[frequency].append(number) 
        
        result = []
        for i in range(len(frequency_array) - 1, 0, -1):
            for number in frequency_array[i]:
                result.append(number)
                if len(result) == k:
                    return result

