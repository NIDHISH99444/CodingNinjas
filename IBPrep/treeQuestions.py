class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    if not root :
        return
    queue=[root]
    ll=[]
    while queue:
        res=[]
        for i in range(len(queue)):
            node=queue.pop(0)
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ll.append(res)
        res=[]
    return ll

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)

print(levelOrderTraversal(root))