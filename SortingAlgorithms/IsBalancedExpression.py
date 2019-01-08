def checkIsValid(p1,p2):
    if p1=="]" and p2=="[":
        return True
    elif p1=="}" and p2=="{":
        return True
    elif p1==")" and p2=="(":
        return True
    else: return False

def is_balanced_expression(expression):
    is_valid=True
    stackList=[]

    for s in expression:
        if s in "[{(":
            stackList.append(s)
        elif s in ")}]":
            is_valid = checkIsValid(s,stackList.pop())
            if is_valid==False:
                return is_valid

    if len(stackList)==0:
        return True
    else:
        return False

expression = ""
print(is_balanced_expression(expression))