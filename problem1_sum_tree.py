r"""
Given a root node of a binary tree, write a function that converts the binary tree to
a tree where each node is the sum of all its children. For example, if the original
tree is:


      8
    /   \
  -2     4
 / \    / \
5   1  2  -7

The new tree would be:

	     3 (5+1-2+2-7+4)
	   /   \
(5+1) 6     -5 (2-7)
	 / \    / \
	0   0  0   0
"""


class TreeNode:  # pylint: disable=too-few-public-methods
    """
    Node defintion
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def to_sum_tree(node):
    """
    sum tree logic
    """
    # Base case
    if node is None:
        return 0

    # Store the old value
    old_val = node.data

    # Recursively call for left and
    # right subtrees and store the sum as
    # new value of this node
    node.data = to_sum_tree(node.left) + \
        to_sum_tree(node.right)

    # Return the sum of values of nodes
    # in left and right subtrees and
    # old_value of this node
    return node.data + old_val


def print_in_order(node):
    """
    print tree in order for display
    """
    if node is None:
        return
    print_in_order(node.left)
    print(node.data, end=" ")
    print_in_order(node.right)


def new_node(data):
    """
    define new node
    """
    temp = TreeNode(0)
    temp.data = data
    temp.left = None
    temp.right = None

    return temp


def max_tree_depth(node):
    """
    Compute the "maxDepth" of a tree -- the number of nodes
    along the longest path from the root node down to the
    farthest leaf node
    """
    if node is None:
        return 0

    # Compute the depth of each subtree
    l_depth = max_tree_depth(node.left)
    r_depth = max_tree_depth(node.right)

    return (l_depth if l_depth > r_depth else r_depth) + 1


def get_leaf_nodes(node):
    """
    Get all leaf nodes of a tree
    """

    leaf_nodes = []

    def find_leaf_nodes(node):

        if node is None:
            return

        if node.left is None and node.right is None:
            leaf_nodes.append(node.data)

        if node.left:
            find_leaf_nodes(node.left)

        if node.right:
            find_leaf_nodes(node.right)

    find_leaf_nodes(node)

    return leaf_nodes


if __name__ == "__main__":

    ROOT = None

    ROOT = new_node(8)
    ROOT.left = new_node(-2)
    ROOT.right = new_node(4)
    ROOT.left.left = new_node(5)
    ROOT.left.right = new_node(1)
    ROOT.right.left = new_node(2)
    ROOT.right.right = new_node(-7)

    print(f"Tree Depth: {max_tree_depth(ROOT)}")
    print(f"Leaf Nodes: {get_leaf_nodes(ROOT)}")

    to_sum_tree(ROOT)

    # Print inorder traversal of the converted
    # tree to test result of toSumTree()
    print("Inorder Traversal of the resultant tree is: ")
    print_in_order(ROOT)

    print(f"Sum Tree Depth: {max_tree_depth(ROOT)}")
    print(f"Leaf Nodes: {get_leaf_nodes(ROOT)}")
