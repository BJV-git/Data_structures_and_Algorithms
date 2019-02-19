


class stack_(object):
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def enq(self,val):
        self.instack.append(val)
    def deq(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        self.outstack.pop()