import  collections

# the only logic is that we gonna popleft and append till we get the pushed elem at front rather last, so we make all the people
# in line to again join the line

# if asked for 2 queues then only for push just create a copy and push, rest use the original queue
class MyStack(object):
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not len(self.q)