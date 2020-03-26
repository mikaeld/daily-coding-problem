package main

// Good morning! Here's your coding interview problem for today.
// This problem was asked by Google.
// Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
// For example, given the following Node class
// ```
// class Node:
//     def __init__(self, val, left=None, right=None):
//         self.val = val
//         self.left = left
//         self.right = right
// ```
// The following test should pass:
// ```
// node = Node('root', Node('left', Node('left.left')), Node('right'))
// assert deserialize(serialize(node)).left.left.val == 'left.left'
// ```

import (
	"fmt"
	"strings"
)

type node struct {
	Value string
	Left  *node
	Right *node
}

func serialize(n *node) string {
	if n == nil {
		return ""
	}

	leftser := serialize(n.Left)
	rightser := serialize(n.Right)

	return n.Value + "," + leftser + "," + rightser
}

func deserialize(data string) *node {
	slice := strings.Split(data, ",")
	fmt.Printf("%v\n", slice)
	n := deserializeSlice(slice)

	return n
}

func deserializeSlice(data []string) *node {

	// Get value and pop
	popVal := data[:1]
	data = data[1:]

	if popVal[0] == "" {
		return nil
	}

	n := node{}
	n.Value = popVal[0]
	n.Left = deserializeSlice(data)
	n.Right = deserializeSlice(data)

	return &n
}

func main() {
	n := node{"root", &node{"left", &node{"left.left", nil, nil}, nil}, &node{"right", nil, nil}}
	fmt.Printf("Check: %v\n", deserialize(serialize(&n)).Left.Left.Value == "left.left")
}
