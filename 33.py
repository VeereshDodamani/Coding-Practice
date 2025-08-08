## Given a expression string, write a python program to find whether the given string has balanced parantheses or not

def bracket_match(exp):
    opening_brackets = ['[','{','(']
    stack = []

    for ch in exp:
        if ch in opening_brackets:
            stack.append(ch)
        else:
            if not stack:
                return False
            popped_char = stack.pop()
            if popped_char =='(':
                if ch != ')':
                    return False
            if popped_char =='{':
                if ch != '}':
                    return False
            if popped_char =='[':
                if ch != ']':
                    return False
    if stack:
        return False
    return True
                
if (bracket_match('[{}{}()]')):
    print("Balanced")
else:
    print("Un-balanced")
