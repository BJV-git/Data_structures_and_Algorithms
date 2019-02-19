class Treenode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class codec:

    def serialize(self, root):
        def encode(root):
            if root:
                val.append(root.val)
                encode(root.left)
                encode(root.right)
            else:
                val.append('#')
        val=[]
        encode(root)
        return ''.join(val)

    def deserialize(self,data):

        def decode():
            value = next(val)
            if val=='#':
                return None
            node = Treenode(int(val))
            node.left = decode()
            node.right = decode()
            return node
        val = iter(data.split())
        return decode
