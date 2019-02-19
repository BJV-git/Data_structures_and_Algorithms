# can use lca and measure the distance

def LCA(root, c1,c2):
    pass

def distance(root, n1,n2):

    def find_d(root, data, d, level):
        if not root:
            return
        if root.val == data:
            d.append(level)
            return

        find_d(root.left,data,d, level+1)
        find_d(root.right, data, d, level + 1)

    lca =LCA(root,n1,n2)
    if not lca:
        return -1
    d1=[]
    d2=[]
    find_d(lca,n1,d1,0); find_d(lca,n2,d2,0)
    return d1[0] + d2[0]
