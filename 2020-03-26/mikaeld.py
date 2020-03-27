"""
author: mikaeld
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    result = ''
    if root:
        result = f'{result},{root.val}' if result else f'{root.val}'
        result = f'{result},{serialize(root.left)}'
        result = f'{result},{serialize(root.right)}'
    else:
        result = f'{result},None' if result else 'None'
    return result


def deserialize(s: str) -> Node:
    def decode(nodes):
        current = next(nodes)
        if current == 'None':
            return None
        node = Node(val=current)
        node.left = decode(nodes)
        node.right = decode(nodes)
        return node

    nodes = iter(s.split(','))
    return decode(nodes)


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serial = serialize(node)
    deserial = deserialize(serial)

    assert deserialize(serialize(node)).left.left.val == 'left.left'