class TrieNode():
    def __init__(self):
        self.child={}
        self.last=False

class Trie():

    def __init__(self):
        self.root = TrieNode()
        self.words=[]

    def form(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root
        for a in key:
            if not self.node.child.get(a):
                node.child[a] = TrieNode()

            node = node.child[a]
        node.last = True

    def search(self, key):
        node = self.root
        found = True

        for a in key:
            if not node.child.get(a):
                found=False
                break
            node = node.child[a]

        return node and node.last and found


    def suggest(self, node, word):
        if node.last:
            self.words.append(word)

        for a,n in node.child.items():
            self.suggest(n, word+a)

    def print(self, key):

        node = self.root
        not_found = False
        temp=''

        for a in key:
            if not node.child.get(a):
                not_found=True
                break
            temp+=a
            node = node.child[a]

        if not_found:
            return 0

        elif node.last and not node.child:
            return -1

        self.suggest(node, temp)

        for s in self.words:
            print(s)
        return 1