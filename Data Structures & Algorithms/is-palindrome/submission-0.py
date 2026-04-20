# basic solution:
# 1. remove all spaces, and inverse alphanumeric characters
# 2. compare this with the reversed string. if they are teh same, then its a palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:  
        new_string = ""
        for character in s:
            if character.isalnum(): 
                new_string += character.lower() 
        return new_string == new_string[::-1]


# other solution: using two pointers.