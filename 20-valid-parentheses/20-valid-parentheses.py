class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list(s)
        stack = []
        
        for i in l :
            if i in ['(', '{', '['] :
                stack.append(i)
            else :
                if len(stack) == 0 :
                    return False
                elif stack[len(stack) - 1] == '(' and i == ')' :
                    stack.pop()
                elif stack[len(stack) - 1] == '[' and i == ']' :
                    stack.pop()
                elif stack[len(stack) - 1] == '{' and i == '}' :
                    stack.pop()
                else :
                    return False
        if len(stack) > 0 :
            return False
        else :
            return True