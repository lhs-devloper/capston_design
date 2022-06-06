class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


def preorder(node):
    if node == None:
        return
    print(node.data, end="-->")
    preorder(node.left)
    preorder(node.right)


def con(new):
    global root
    current = root

    while True:
        if new.data < current.data:
            if current.left == None:
                current.left = new
                break
            current = current.left

        else:
            if current.right == None:
                current.right = new
                break
            current = current.right


node1 = TreeNode()
node2 = TreeNode()
node3 = TreeNode()
node4 = TreeNode()
node5 = TreeNode()
node1.data = 10
node2.data = 8
node1.left = node2
node3.data = 15
node1.right = node3
node4.data = 3
node2.left = node4
node5.data = 9
node2.right = node5
root = node1
preorder(root)

newnode = TreeNode()
a = int(input("입력"))
newnode.data = a
con(newnode)
preorder(root)
print("끝")


newnode2 = TreeNode()
a1 = int(input("입력"))
newnode2.data = a1


con(newnode2)
preorder(root)
print("끝")


newnode3 = TreeNode()
a2 = int(input("입력"))
newnode3.data = a2

con(newnode3)
preorder(root)
print("끝")
