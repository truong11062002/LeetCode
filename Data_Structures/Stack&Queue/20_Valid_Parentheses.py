def isValid(s):
    leftSymbols = []
    for c in s:
        if c in ['(', '[', '{']:
            leftSymbols.append(c)
            
        elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
            leftSymbols.pop()
        elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
            leftSymbols.pop()
        elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
            leftSymbols.pop()
        else:
            return False
    if len(leftSymbols) == 0:
        return True

s = "{[]}"
print(isValid(s))
    