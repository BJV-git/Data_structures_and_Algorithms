

def num_to_roman(n):

    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    res=''
    romans=["", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i=0
    while n:
        res+= (n//values[i])*romans[i]
        n %= values[i]
        i+=1
    return res


print(num_to_roman(45))