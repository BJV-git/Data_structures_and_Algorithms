def decodings(s):
    v,w,p = 0,int(s>''), ''
    for d in s:
        v,w,p = w, (d>'0')*w + (9<int(p+d)<27)*v,d  # making sure if we can see the number falling with in teh range of mapping
    return w