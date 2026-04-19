# naive solution: traverse through each string, sort that string, and then sort each string and hceck if its the same , if it is, then string them together.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        result = defaultdict(list) #character_count_of_each_string : mapping to list of anagrams 

        for s in strs:
            count = [0] * 26 # a...z 
            for c in s:
                count[ord(c) - ord('a')] += 1 
            result[tuple(count)].append(s) 
        return list(result.values())
        