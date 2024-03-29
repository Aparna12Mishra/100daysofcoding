class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                        
        d = {")": "(", "}": "{", "]": "["}  

        for x in s:
            if x in d:                      
                if stack and stack[-1] == d[x]:
                    stack.pop()              
                else:
                    return False           
            else:
                stack.append(x)             
        return not stack