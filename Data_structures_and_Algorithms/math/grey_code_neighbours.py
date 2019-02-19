# can shift numbers and see if they are

def grey_neghbours(a,b):
    diff=0
    while (a>0 or b>0):
        if (a&1)!=(b&1):
            diff+=1
            if diff>1:
                return False
    return True