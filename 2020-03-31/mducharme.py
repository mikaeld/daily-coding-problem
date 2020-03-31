"""
author: mikaeld
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_unival(node: Node, parent_value: int) -> bool:
    if node is None:
        return True

    if node.value == parent_value:
        return is_unival(node.left, node.value) and is_unival(node.right, node.value)

    return False


def count_unival_subtrees(node: Node) -> int:
    if node is None:
        return 0

    if is_unival(node, node.value):
        return count_unival_subtrees(node.left) + count_unival_subtrees(node.right) + 1

    return count_unival_subtrees(node.left) + count_unival_subtrees(node.right)


if __name__ == '__main__':
    root = (Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))))

    assert count_unival_subtrees(root) == 5
