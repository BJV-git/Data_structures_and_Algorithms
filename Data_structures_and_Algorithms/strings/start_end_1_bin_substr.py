# technique : if n return n(n-1)//2

def countsubstr(st):
    count=0
    for i in st:
        if i=='1':
            count+=1

    return count*(count-1)//2