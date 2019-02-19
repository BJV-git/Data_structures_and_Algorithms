def valid_paranthesis(s):
    stack=[]
    open=set(['{','(','['])
    close = set(['}',']',')'])

    dic = {'}': '{', ')': '(', ']': '['}

    for brac in s:
        if brac in open:
            stack.append(brac)
        elif brac in close:
            if not stack or stack.pop() != dic[brac]:
                return False

    return not stack  # extra braces i.e. just the closed ones