s = input()
n = int(s.split(" ")[0])
m = int(s.split(" ")[1])

# 输入权重和父节点信息
weights = list(map(int, input().split(" ")))
parents = list(map(int, input().split(" ")))



# 建立树
class TreeNode:
    def __init__(self, val=0):
        self.val = val  # 节点的权重
        self.left = None  # 左子节点
        self.right = None  # 右子节点

def buildTree(weights, parents):
    nodes = [None]*(len(weights))
    for i in range(len(weights)):
        nodes[i] = TreeNode(weights[i])
    # 根据父节点信息构建树
    for i in range(len(parents)):
        parent_idx = parents[i]-1  # 父节点索引
        if nodes[parent_idx].left is None:
            nodes[parent_idx].left = nodes[i+1]  # 第一个子节点放在左边
        else:
            nodes[parent_idx].right = nodes[i+1]  # 第二个子节点放在右边

    return nodes  # 返回树

# 删除节点
def deleteNode(root,nodeidx):
    parentidx = parents[nodeidx-1]-1
    if root[parentidx].left == root[nodeidx]:
        root[parentidx].left = None
    else:
        root[parentidx].right = None


# 查找是否是子节点
def isChild(root, node):
    if root is None:
        return False
    if root == node:
        return True
    return isChild(root.left, node) or isChild(root.right, node)

# 遍历求权重
def weightSum(root):
    if root is None:
        return 0
    sum = root.val
    return sum + weightSum(root.left)+weightSum(root.right)

# 计算权重差
def weightDiff(root,node,weight,sum):
    if node is None:
        return
    weight.append([root.index(node)+1,abs(2*weightSum(node)-sum)])
    weightDiff(root,node.left,weight,sum)
    weightDiff(root,node.right,weight,sum)


for i in range(m):
    test = int(input())
    rootidx = 0
    root = buildTree(weights, parents)
    weights1 = []
    weightDiff(root, root[rootidx], weights1, weightSum(root[rootidx]))
    result,minval = min(weights1,key=lambda x:x[1])
    print(result,end=" ")
    while True :
        if isChild(root[result - 1], root[test - 1]):#是结果节点或其子节点
            rootidx = result-1 #改根节点
        else:
            deleteNode(root,result-1) #删除节点
        weights1 = []
        weightDiff(root, root[rootidx], weights1, weightSum(root[rootidx]))
        if len(weights1)==1:
            break
        result, minval = min(weights1, key=lambda x: x[1])
        print(result, end=" ")
    print()