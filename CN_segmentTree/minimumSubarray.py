import sys
def buildTree(arr,tree,start,end,treeNode):
    if start==end:
        tree[treeNode]=arr[start]
        return
    mid=(start+end)//2
    buildTree(arr,tree,start,mid,2*treeNode)
    buildTree(arr,tree,mid+1,end,2*treeNode+1)
    tree[treeNode]=min(tree[treeNode*2],tree[treeNode*2+1])

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
        return sys.maxsize
    #completely insdie given range
    if start>=left and end<=right:
        return tree[treeNode]
    #partially inside and partially outside
    mid=(start+end)//2
    ans1=queryTree(tree,start,mid,2*treeNode,left,right)
    ans2=queryTree(tree,mid+1,end,2*treeNode+1,left,right)
    return min(ans1,ans2)

# n,m=list(map(int,input().split()))
# arr=list(map(int,input().split()))
arr=[1,5,2,4,3]
tree=[0]*(len(arr)*4)
buildTree(arr,tree,0,len(arr)-1,1)
#
# for i in range(m):
#     a,b,c=input().split()
#     if a=='q':
#         ans = queryTree(tree, 0, len(arr)-1, 1, int(b)-1,int(c)-1)
#         print(ans)
#     elif a=='u':
#         updateTree(arr, tree, 0, len(arr)-1, 1,int(b)-1,int(c)-1)
#         print(tree)
 
# 5 11
# 1 5 2 4 3
# q 1 5         1
# q 1 3         1
# q 3 5         2
# u 3 6
# q 1 5         1
# u 3 100
# q 1 2         1
# q 2 4         4
# q 4 5         3
# u 3 1
# q 1 5         1