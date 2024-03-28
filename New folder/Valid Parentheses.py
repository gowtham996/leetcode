class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                l.append(i)
            elif i == ')' or i == '}' or i == ']':
                if not l or (i == ')' and l[-1] != '(') or (i == '}' and l[-1] != '{') or (i == ']' and l[-1] != '['):
                    return False
                l.pop()
        return not l
            
            