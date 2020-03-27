class Node :
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def SortedArrayToBST(arr):
    if not arr:
        return
    mid=len(arr)//2

    root=Node(arr[mid])
    root.left=SortedArrayToBST(arr[:mid])
    root.right = SortedArrayToBST(arr[mid+1:])
    return root

def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data,end=" ")
    printInorder(root.right)


arr = [1, 2, 3, 4, 5, 6, 7]
root=SortedArrayToBST(arr)
printInorder(root)

