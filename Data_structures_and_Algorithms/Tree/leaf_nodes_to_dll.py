# for only capturing the leafs only in the left to right order lets go with the in order and make sure while
# capturing its a leaf and then in every step lets form or build the double linked list

# only modification is that as we are inserting in back ways need to traverse from right ot left
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def leaves_to_dll(root):
    if not root: return None

    if not root.left and not root.right:
        root.right = leaves_to_dll.head
    if leaves_to_dll.head:
        leaves_to_dll.head.left = root
    leaves_to_dll.head = root

    leaves_to_dll(root.right)
    leaves_to_dll(root.left)

    return root





leaves_to_dll.head = Node(None)