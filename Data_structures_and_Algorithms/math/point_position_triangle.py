def point_lies(a,b,c,p):
    def area(a,b,c):
        return abs((a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(b[1]-c[1]) )/2.0)


    return area(a,b,c) == area(p,a,b) +  area(p,b,c) + area(p,a,c)