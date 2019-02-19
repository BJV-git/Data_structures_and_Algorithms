# logic: the first left bottom shud be less than the second right top and second left bottom shud be < first top right

def isoverlap(rec1,rec2):
    return rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec2[0] < rec1[2] and rec2[1] < rec1[3]