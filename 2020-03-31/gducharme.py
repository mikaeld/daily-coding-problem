#not my solution: https://www.dailycodingproblem.com/blog/unival-trees/


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))


def is_unival(node):
    return unival_helper(node, node.val)


def unival_helper(node, value):
    if node is None:
        return True
    if node.val == value:
        return unival_helper(node.left, value) and unival_helper(node.right, value)


def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return left + right + (1 if is_unival(root) else 0)

if __name__ == '__main__':
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    assert count_unival_subtrees(root) == 5