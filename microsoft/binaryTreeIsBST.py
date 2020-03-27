
INT_MIN = -2147483648
INT_MAX = 2147483647


class newNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def largestBSTBT(root):

    if (root == None):
        return False,0, 0, 0
    if (root.left == None and root.right == None):
        return True,1, root.data, root.data

    # Recur for left subtree and right subtrees
    l = largestBSTBT(root.left)
    r = largestBSTBT(root.right)


    ret = [0, 0, 0, 0, 0]
    ret[1] = (1 + l[1] + r[1])

    # If whole tree rooted under current root is
    # BST.
    if (l[0] and r[0] and l[3] <
            root.data and r[2] > root.data):
        ret[2] = min(l[2], root.data)
        ret[3] = max(r[3], root.data)
        ret[0] = True

        return ret

    ret[1] = max(l[1], r[1])
    ret[0] = l[0] and r[0]

    return ret


# Driver Code
if __name__ == '__main__':
    """Let us construct the following Tree 
        60 
        / \ 
        65 70 
    / 
    50 """
    root = newNode(60)
    root.left = newNode(65)
    root.right = newNode(70)
    root.left.left = newNode(50)
    print("Size of the largest BST is",
          largestBSTBT(root)[1])


