# 1. first check: the length of the strings is same, if not, then retur false. 
# 2. create dictionaries, and the dictionaries should be the same
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s) != len(t):
            return False 
        else:  
            first_counter = Counter(s)
            second_counter = Counter(t)
            if first_counter == second_counter:
                return True 
            else:
                return False 


        