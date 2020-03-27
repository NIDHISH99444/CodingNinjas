
import sys

def buildTree(arr,tree,start,end,treeNode):
    if start==end:
        tree[treeNode]=[arr[start],-sys.maxsize]
        return
    mid=(start+end)//2
    buildTree(arr,tree,start,mid,2*treeNode)
    buildTree(arr,tree,mid+1,end,2*treeNode+1)
    first=max(tree[2*treeNode][0],tree[2*treeNode+1][0])
    second=min(max(tree[2*treeNode][0],tree[2*treeNode+1][1]),max(tree[2*treeNode+1][0],tree[2*treeNode][1]))
    tree[treeNode]=[first,second]

def updateTree(arr,tree,start,end,treeNode,index,val):
    if start==end:
        arr[index]=val
        tree[treeNode]=val
        return
    mid=(start+end)//2
    if mid>=index:
        updateTree(arr,tree,start,mid,2*treeNode,index,val)
    else:
        updateTree(arr,tree,mid+1,end,2*treeNode+1,index,val)
    tree[treeNode]=min(tree[treeNode*2],tree[treeNode*2+1])


def queryTree(tree,start,end,treeNode,left,right):


    #completely outside given range
    if start>right or end<left:
        return [-sys.maxsize,-sys.maxsize]
    #completely insdie given range
    if start>=left and end<=right:
        return tree[treeNode]
    #partially inside and partially outside
    mid=(start+end)//2
    ans1=queryTree(tree,start,mid,2*treeNode,left,right)
    ans2=queryTree(tree,mid+1,end,2*treeNode+1,left,right)
    first = max()
    second = min(max(tree[2 * treeNode][0], tree[2 * treeNode + 1][1]),
                 max(tree[2 * treeNode + 1][0], tree[2 * treeNode][1]))
    tree[treeNode] = [first, second]
    return tree[treeNode]

arr=[1,3,2,4,5]
tree=[0]*(len(arr)*4)
buildTree(arr,tree,0,len(arr)-1,1)
print(tree)



