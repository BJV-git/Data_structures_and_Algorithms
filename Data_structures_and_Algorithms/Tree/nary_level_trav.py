# just instead of the in (left , right) will go for .children the array

def levelOrder(self, root):
    if not root: return []
    queue = [root]
    self.res = []
    while queue:
        self.res.append([i.val for i in queue])
        queue = [child for node in queue for child in node.children]
    return self.res