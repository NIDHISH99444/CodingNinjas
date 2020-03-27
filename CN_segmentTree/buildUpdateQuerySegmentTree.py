def buildTree(arr,tree,start,end,treeNode):
    if start==end:
        tree[treeNode]=arr[start]
        return
    mid=(start+end)//2
    buildTree(arr,tree,start,mid,2*treeNode)
    buildTree(arr,tree,mid+1,end,2*treeNode+1)
    tree[treeNode]=tree[treeNode*2]+tree[treeNode*2+1]

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
    tree[treeNode]=tree[treeNode*2]+tree[treeNode*2+1]


def queryTree(tree,start,end,treeNode,left,right):


    #completely outside given range
    if start>right or end<left:
        return 0
    #completely insdie given range
    if start>=left and end<=right:
        return tree[treeNode]
    #partially inside and partially outside
    mid=(start+end)//2
    ans1=queryTree(tree,start,mid,2*treeNode,left,right)
    ans2=queryTree(tree,mid+1,end,2*treeNode+1,left,right)
    return ans1+ans2


arr=[1,2,3,4,5]
tree=[0]*(len(arr)*2)
buildTree(arr,tree,0,4,1)
for  i in range(1,len(tree)):
    print(tree[i],end=" ")
updateTree(arr,tree,0,4,1,2,10)
print()
for  i in range(1,len(tree)):
    print(tree[i],end=" ")
ans=queryTree(tree,0,4,1,2,4)
print()
print("Sum between interval",ans)