# plain logic, is to keep the top frequent ones in a seperate list and just print all time

class top_k(object):
    def __init__(self, k):
        self.top_l = 0
        self.k = k
        self.freq={}
        self.top=[]

    def add(self, n):
        self.freq[n] = self.freq.get(n,0)+1
        self.top_l+=1

        if self.top_l < self.k: # we might need to filter before printing
            self.top.append(n)
        elif self.freq[n] > self.freq[self.top[-1]]:
            self.top.pop()
            self.top.append(n)

        self.top.sort(key=lambda x: self.freq[x], reverse=True)


        print(self.top)