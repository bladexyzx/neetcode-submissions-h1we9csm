class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if len(stack) == 0 and bracket in ["}", ")", "]"]:
                return False
            if bracket in ["{", "(", "["]:
                stack.append(bracket)
            if bracket == "}":            
                if stack[-1] == "{":
                    stack.pop(-1)
                    continue
                else:
                    return False
            if bracket == "]":            
                if stack[-1] == "[":
                    stack.pop(-1)
                    continue
                else:
                    return False
            if bracket == ")":            
                if stack[-1] == "(":
                    stack.pop(-1)
                    continue
                else:
                    return  False
        if len(stack) == 0:
            return True
        else:
            return False