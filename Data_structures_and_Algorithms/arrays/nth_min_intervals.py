# mergeg the intervals and count ahead

intervals = [(5,10), (15,20), (25,40),(30,45),(50,100)]

end={}

for start in (i[0] for i in intervals):
    end[start] = end.setdefault(start,0)+1
for limit in ( i[1]+1 for i in intervals):
    end[limit] = end.setdefault(limit,0)-1

sorted(filter(lambda x: x[1] != 0, end.items()))

print(end)