# 1. first check: the length of the strings is same, if not, then retur false. 
# 2. create dictionaries, and the dictionaries should be the same

# probably cheating in intevriew to use this
# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool: 
#         if len(s) != len(t):
#             return False 
#         else:  
#             first_counter = Counter(s)
#             second_counter = Counter(t)
#             if first_counter == second_counter:
#                 return True 
#             else:
#                 return False 


# use sorted list 
# time complexity of sorting: depending on sorting algorithm. bnest case is O(Nlogn + Mlogm). something like bubble sort is like O(n^2)
# space complexity is iffy. sometimes they use extra memory o(n +m), sometimes thye can be optimized O(1)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool: 
#         if len(s) != len(t):
#             return False 
#         else:  
#             return sorted(s) == sorted(t)


# using hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s) != len(t):
            return False 
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0) 
        return countS == countT

