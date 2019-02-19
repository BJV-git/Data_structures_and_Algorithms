# use the number as index to track the presence of number by adding len(arr) as we subtracted the 1

def count_freq(arr):
    n=len(arr)

    arr=[i-1 for i in arr] # for index and also while //ing
    for i in range(n):
        arr[arr[i]%n] = arr[arr[i]%n] + n

    for i in range(n):
        print(i+1, arr[i]//n)