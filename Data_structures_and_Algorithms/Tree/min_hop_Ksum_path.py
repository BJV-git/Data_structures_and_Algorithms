# can use the same technique  to count the number of paths to get the count
from collections import deque
def pathsum(root):
    if not root: return None
    res=[]

    queue = deque([(root,[])])
