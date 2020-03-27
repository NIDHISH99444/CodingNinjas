#binary tree to DLL
#remove all path less than k
#Convert a given binary search tree into balanced binary tree
#64 Interview Preparation- Evalution of expression of expression tree
#67 Interview Preparation- Convert a binary tree to a tree holds children sum property
#68 Interview Preparation- Find multiplication of sums of data at same level in a tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def sizeOfTree(root):
    if not root :
        return 0
    return 1+sizeOfTree(root.left)+sizeOfTree(root.right)

def leftViewUtil(root,level,maxLevel):
    if not root:
        return
    if maxLevel[0]<level:
        print(root.data,end=" ")
        maxLevel[0]=level
    leftViewUtil(root.left,level+1,maxLevel)
    leftViewUtil(root.right,level+1,maxLevel)

def leftView(root):
    if not root :
        return
    max_level=[0]
    leftViewUtil(root,1,max_level)

def rightViewUtil(root,level,maxLevel):
    if not root:
        return
    if maxLevel[0]<level:
        print(root.data,end=" ")
        maxLevel[0]=level
    rightViewUtil(root.right,level+1,maxLevel)
    rightViewUtil(root.left, level + 1, maxLevel)

def rightView(root):
    if not root :
        return
    maxLevel=[0]
    rightViewUtil(root,1,maxLevel)

def checkIdentical(root,root1):
    if  root is None and root1 is None:
        return True
    if root is None or root1 is None:
        return False

    return root.data==root1.data and checkIdentical(root.left,root1.left) and checkIdentical(root.right,root1.right)


def mirroringOfTree(root):
    if not root:
        return
    mirroringOfTree(root.left)
    mirroringOfTree(root.right)
    root.left,root.right=root.right,root.left

def inOrder(node):
    if (node == None):
        return
    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)

def levelOrderTraversal(root):
    if not root :
        return
    queue=[root]
    while queue:
        node=queue.pop(0)
        print(node.data,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def lca(root,a,b):
    if not root:
        return
    if root.data==a or root.data==b:
        return root
    left=lca(root.left,a,b)
    right=lca(root.right,a,b)
    if  left and right:
        return root.data
    return left or right

def height(root):
    if not root:
        return 0
    return max(height(root.left),height(root.right))+1

def diameter(root):
    if not root:
        return 0
    ldiameter=diameter(root.left)
    rdiameter=diameter(root.right)
    lheight=height(root.left)
    rheight=height(root.right)
    return max((lheight+rheight+1),ldiameter,rdiameter)

def nodeKDistRoot(root,k):
    if not root or k<0:
        return
    if k==0:
        print(root.data,end=" ")

    nodeKDistRoot(root.left,k-1)
    nodeKDistRoot(root.right,k-1)

def nodeKDistFromNodeDown(root,target,k):
    if not root:
        return
    if root.data==target:
        nodeKDistRoot(root,k)

    nodeKDistFromNodeDown(root.left,target,k)
    nodeKDistFromNodeDown(root.right, target, k)

def AllNodeKDistFromTarget(root,target,k):
    if not root:
        return
    if k==0:
        print(root.data,end=" ")
    if root.data==target:
        nodeKDistRoot(root,k)
        return 0
    dl=AllNodeKDistFromTarget(root.left,target,k)
    if dl!=-1:
        if dl+1==k:
            print(root.data)
        else:
            nodeKDistRoot(root.right,k-dl-2)
        return 1+dl
    dr = AllNodeKDistFromTarget(root.left, target,k)
    if dr != -1:
        if dr + 1 == k:
            print(root.data)
        else:
            nodeKDistRoot(root.left, k - dr - 2)
        return 1 + dr
    return -1

def vertical(root,dict,hd):
    if not root :
        return
    try:
        dict[hd].append(root.data)
    except:
        dict[hd]=[root.data]
    vertical(root.left,dict,hd-1)
    vertical(root.right,dict,hd+1)

def printVertical(root):
    if not root:
        return
    dict={}
    hd=0
    vertical(root,dict,hd)
    for key,value in sorted(dict.items()):
        for i in value:
            print(i,end=" ")
        print()

def printVerticalSum(root):
    if not root:
        return
    dict={}
    hd=0
    vertical(root,dict,hd)
    for key,value in sorted(dict.items()):
        sum=0
        for i in value:
            sum+=i
        print(sum)

def printTopBottomView(root):
    if not root:
        return
    dict={}
    hd=0
    vertical(root,dict,hd)
    topView = []
    bottomView = []
    for key,value in sorted(dict.items()):

            topView.append(value[0])
            bottomView.append(value[-1])
    print("topview is")
    print(topView)
    print("bottom is" )
    print(bottomView)

def isSubTreeCheck(root,subTree):
    if not subTree:
        return True
    if not root:
        return False
    if checkIdentical(root,subTree):
        return True
    return isSubTreeCheck(root.left,subTree) or isSubTreeCheck(root.right,subTree)


def sibling(root,a,b):
    if not root:
        return False
    if root.left and root.right:
        if (root.left.data==a and root.right.data==b ) or (root.left.data==b and root.right.data==a ):
            return True
    return sibling(root.left,a,b) or sibling(root.right,a,b)

def levelCheck(root1,a,level):
    if not root1 :
        return 0
    if root1.data==a:
        return level
    return levelCheck(root1.left,a,level+1) or levelCheck(root1.right, a, level+1)
def checkCousins(root1,a,b):
    if not root1 :
        return
    if (levelCheck(root1,a,1)==levelCheck(root1,b,1)) and not sibling(root1,a,b):
        return True
    return False


def printPath(root):
    path=[0]*100
    printPathRec(root,path,0)

def printPathRec(root,path,pathlen):
    if not root:
        return

    path[pathlen]=root.data

    if root.left is None and root.right is None:
        printPathArray(path,pathlen)
    else:
        printPathRec(root.left,path,pathlen+1)
        printPathRec(root.right,path,pathlen+1)

def printPathArray(path,pathlen):
    for i in range(pathlen+1):
        print(path[i],end=" ")
    print()

def printLevelOrderSpiral(root):
    if not root :
        return
    stack1,stack2=[root],[]
    while stack1 or stack2:
        while stack1:
            node=stack1.pop()
            print(node.data,end=" ")
            if node.right:
                stack2.append(node.right)
            if node.left:
                stack2.append(node.left)
        while stack2:
            node = stack2.pop()
            print(node.data, end=" ")
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

def kdistanceFromLeafUtil(root,k,visited,path,pathlen):
    if not root:
        return
    path[pathlen]=root.data
    visited[pathlen]=False
    if root.left is None and root.right is None and path[pathlen-k]>=0 and visited[pathlen-k]==False:
        visited[pathlen-k]=True
        print(path[pathlen-k],end=" ")
    kdistanceFromLeafUtil(root.left,k,visited,path,pathlen+1)
    kdistanceFromLeafUtil(root.right, k, visited, path,pathlen+1)


def kdistanceFromLeaf(root,k):
    MAXLEN=100
    path=[0]*MAXLEN
    visited=[0]*MAXLEN
    kdistanceFromLeafUtil(root,k,visited,path,0)


def printdiagonalUtil(root,dict,hd):
    if not root :
        return
    if hd not in dict :
        dict[hd] = [root.data]
    else:
        dict[hd].append(root.data)
    printdiagonalUtil(root.left,dict,hd+1)
    printdiagonalUtil(root.right, dict, hd)
def printDiagonal(root):
    if not root :
        return
    dict={}
    hd=0
    printdiagonalUtil(root,dict,hd)
    for key,val in dict.items():
        for ele in val:
            print(ele,end=" ")
        print()

def printExtermeNodeAlternativeUtil(root):
    if not root :
        return
    q,res=[root],[]
    while q:
        level=[]
        for _ in range(len(q)):
            node=q.pop(0)
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

def printExtermeNodeAlternative(root):
    res=printExtermeNodeAlternativeUtil(root)
    flag=0
    for x in res:
        if flag==0:
            print(x[0],end=" ")
            flag=1
        else:
            print(x[-1],end=" ")
            flag=0

def isFoldableUtil(root,root1):
    if root is None and root1 is None:
        return True
    if root is None or  root1 is None:
        return False
    return isFoldableUtil(root.left,root1.right) and  isFoldableUtil(root.right,root1.left)

def isFoldable(root):
    if not root:
        return
    if isFoldableUtil(root.left,root.right):
        return True
    return False
def printLeaf(root):
    if not root:
        return
    if root.left is None and root.right is None:
        print(root.data,end=" ")
    printLeaf(root.left)
    printLeaf(root.right)

def printLeftBoudary(root):
    if not root:
        return
    if root:
        if root.left:
            print(root.data,end=" ")
            printLeftBoudary(root.left)
        elif root.right:
            print(root.data,end=" ")
            printLeftBoudary(root.right)

def printRightBoundary(root):
    if not root :
        return
    if root:
        if root.right:
            printRightBoundary(root.right)
            print(root.data,end=" ")
        elif root.left:
            printRightBoundary(root.left)
            print(root.data,end=" ")
def printBoundary(root1):
    if not root:
        return
    printLeftBoudary(root1)
    printLeaf(root1)
    printRightBoundary(root1.right)

def sumCalc(root):
    if not root :
        return 0
    return root.data+sumCalc(root.left)+sumCalc(root.right)
def checkSumTree(root):
    if not root :
        return True
    if root.left is None and root.right is None:
        return True
    lft=sumCalc(root.left)
    rgt=sumCalc(root.right)
    if (root.data==lft+rgt) and checkSumTree(root.left) and checkSumTree(root.right):
        return True
    return False

def ansestors(root,node,res=[]):
    if not root :
        return False
    if root.data==node :
        res.append(root.data)
        return True
    if ansestors(root.left,node,res):
        res.append(root.data)
        return True
    if ansestors(root.right,node,res):
        res.append(root.data)
        return True
    return False


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)


root1 = Node(8)
root1.left = Node(3)
root1.right = Node(10)
root1.left.left = Node(1)
root1.left.right = Node(6)
root1.right.left = Node(7)
root1.right.right = Node(9)

subTree = Node(26)
subTree.left = Node(10)
subTree.right = Node(3)
subTree.left.left=Node(4)
subTree.left.right=Node(6)
subTree.right.left=Node(3)


print("-----------------------------------")
print("Size of tree is ")
print(sizeOfTree(root))
print("-----------------------------------")
print("Left view of tree is")
leftView(root)
print()
print("-----------------------------------")
print("Right view of tree is")
rightView(root)
print()
print("-----------------------------------")
print("Check tree are identical ")
print(checkIdentical(root,root1))
print("-----------------------------------")
print("Level Order traversal  of Tree ")
levelOrderTraversal(root)
# print("-----------------------------------")
# print("Check mirror of Tree ")
# print("Before mirroring inorder traversal")
# inOrder(root)
# mirroringOfTree(root)
# print()
# print("After mirroring inorder traversal")
# inOrder(root)
print()
print("-----------------------------------")
print("LCA  of %d and %d is %d"%(6,10,lca(root,6,10)))
print("-----------------------------------")
print("Diamaeter of binary tree ")
print(diameter(root))
print("-----------------------------------")
print("Nodes k distance from root")
nodeKDistRoot(root,1)
print()
print("-----------------------------------")

print("Nodes %d distance from node %d are" % (1,3),end=" ")
nodeKDistFromNodeDown(root,3,1)
print()
print("-----------------------------------")
print("Nodes k distance from target in all directions")
AllNodeKDistFromTarget(root,3,1)

print("-----------------------------------")
print("Vertical traversal ")
printVertical(root)

print("-----------------------------------")
print("Vertical traversal Sum ")
printVerticalSum(root)
print("-----------------------------------")
print("Vertical traversal Sum ")
printTopBottomView(root)
print("-----------------------------------")
print("Check Subtree ")
print(isSubTreeCheck(root,subTree))
print("-----------------------------------")
print("Check cousins ")

print(checkCousins(root1,1,7))
print("-----------------------------------")
print("Print all root to leaf paths  ")
printPath(root1)
print("-----------------------------------")
print("Check cousins ")
print(checkCousins(root1,1,10))

print("-----------------------------------")
print("Print spiral order of tree")
printLevelOrderSpiral(root1)
print()
print("-----------------------------------")
print("K distance from leaf ")
kdistanceFromLeaf(root1,1)
print()
print("-----------------------------------")
print("Diagonal traversal of node")
printDiagonal(root1)
print("-----------------------------------")
print("Print Extreme node at each level in alternative order")
printExtermeNodeAlternative(root1)
print()
print("----------------------------------------------------------------------------------")
print("-----------------------------------")
print("Check if tree is foldable or not ")
print(isFoldable(root1))

print("-----------------------------------")
print("Print boundary Traversal  ")
printBoundary(root1)
print()
print("-----------------------------------")
print("Check Sum Tree")
print(checkSumTree(subTree))
res=[]
print("-----------------------------------")
print("Check all Ancestors")
ansestors(root,6,res)
print(res)
