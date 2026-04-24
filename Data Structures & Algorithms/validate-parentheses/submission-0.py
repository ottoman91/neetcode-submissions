# 1. use a stack and a hashmap 
# 1. every closing parenthesis should be mapped to an opening parenthesis int he correct order

# 1. create a hashmpa : closing parenthesis : opening parenthesis 
# 2. declare a stack
# 2. iterate thhrough each element. 
# if we see a closing parenthesis: 
# if stack is not empty and stack top value is equal to the closing mapping, then we pop and continue, otherwise return false
# if we see an opening parenthesis, add it to the stack. 
# return true if the stack is empty else return false

class Solution:
    def isValid(self, s: str) -> bool: 
        stack = []
        closing_parenthesis_hashmap = {')': '(', '}':'{', ']':'['} 
        for character in s:
            if character in closing_parenthesis_hashmap:
                if stack and stack[-1] == closing_parenthesis_hashmap[character]:
                    stack.pop() 
                else:
                    return False 
            else:
                stack.append(character) 
        return True if not stack else False
        