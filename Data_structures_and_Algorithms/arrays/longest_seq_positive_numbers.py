# logic: if see + increment the count else reset

def longest_pos(nums):
    count=0
    temp=0
    start_ind=0
    temp_ind = 0
    for j,i in enumerate(nums):
        if i>0:
            temp+=1
            if count==1: # so that we only start the index for the positive integer
                temp_ind = j
        else:
            if count < temp:
                count = temp
                start_ind = temp_ind
            temp=0
    return max(count, temp)