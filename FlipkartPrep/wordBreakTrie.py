
class TrieNode:

    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,wordN):
        node=self.root
        for i in wordN:
            if i not in node.children:
              node.children[i]=TrieNode()
            node=node.children[i]
        node.word=True

    def search(self,wordN):
        node = self.root
        for i in wordN:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

def checkWord(str):
    if len(str)==0:
        return True
    for i in range(1,len(str)+1):
        if trie.search(str[:i]) and checkWord(str[i:]):
            return True
    return False
trie = Trie()
def wordBreak(str,list):
    for ele in list:
        trie.insert(ele)
    print(checkWord(str))

wordBreak("bedbathandbeyond", ["teddy", "bath", "bedbath", "and", "beyond"])
#wordBreak("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "away"])

