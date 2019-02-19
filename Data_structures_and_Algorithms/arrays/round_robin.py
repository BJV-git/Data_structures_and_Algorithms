# we assume we have submitted at time 0 all the tasks

def wait_time(process, n, bt, wt, quantum):
    rem_bt = [0]*n

    for i in range(n):
        rem_bt[i] = bt[i]
    t=0

    while (1):
        done = True # before every iteration we set to be true

        for i in range(n):
            if rem_bt[i] > 0:
                done =False # set false, to say some process is remaining

                if (rem_bt[i] > quantum):
                    t+=quantum
                    rem_bt[i]-=quantum
                else:
                    t+=bt[i]
                    wt[i] = t - bt[i] # it has utilized its time any ways and wait time is - of t
                    rem_bt[i]=0

        if done==True:
            break