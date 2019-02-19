# using merkle: which is formed by hashing the left and righ t child and root.val so all we need to see is that if any time
# the two trees have equal merkles

# O(n2) is just write a fucntion to check adn check each node

from hashlib import sha256
def issubtree(s,t):
    def _hash(x):
        s = sha256()
        s.update(x)
        return s.hexdigest()

    def merkle(node):
        if not node: return '#'

        m_l = merkle(node.left)
        m_r = merkle(node.right)

        node.merkle = _hash(m_l + str(node.val) + m_r)

        return node.merkle

    merkle(s)
    merkle(t)

    def dfs(node):
        if not node: return False

        return (node.merkle == t.merkle or dfs(node.left) or dfs(node.right))

