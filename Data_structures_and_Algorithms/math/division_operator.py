# logic: >> will shift the bits and wil use the | operator

def divide(dividend, divisor):
    sign = -1 if dividend*divisor < 0 else 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    q  = 0
    temp =0

    for i in range(31,-1,-1):
        if temp+(divisor<<i) <= dividend: # when ever we feel like possibel for division
            temp += divisor<<i # so we are adding  the possible integers
            q|=1<<i # we are trying to increment the quotient
            print(i, temp,divisor<<i , q, 1<<i)

    return sign*q

print(divide(10,3))