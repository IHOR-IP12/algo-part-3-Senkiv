class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None
def show_tree(root):
    if root:
        show_tree(root.left)
        print(root.value, end="\t")
        show_tree(root.right)
def invert_tree(root):
    if root:
        left = invert_tree(root.left)
        right = invert_tree(root.right)
        root.left = right
        root.right = left
    return root

root = TreeNode(35)
root.left = TreeNode(30)
root.right = TreeNode(40)
root.right.right = TreeNode(42)
root.right.left = TreeNode(37)
root.left.left = TreeNode(22)
root.left.left.left = TreeNode(21)
root.left.left.right = TreeNode(25)
root.left.right = TreeNode(31)
root.left.right.right = TreeNode(32)
root.left.left.right.left =TreeNode(24)
root.left.left.right.left.left =TreeNode(23)
root.left.left.right.right =TreeNode(26)
root.left.left.right.right.right =TreeNode(27)

show_tree(root)
print("not inverted")
invert_tree(root)
show_tree(root)
print("first invert")
invert_tree(root)
show_tree(root)
print("second invert")
