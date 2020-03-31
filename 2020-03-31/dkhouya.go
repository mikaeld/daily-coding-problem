package main

import "fmt"

// Good morning! Here's your coding interview problem for today.
// This problem was asked by Google.
// A unival tree (which stands for "universal value") is a tree where all
// nodes under it have the same value.
// Given the root to a binary tree, count the number of unival subtrees.
// For example, the following tree has 5 unival subtrees:

// ```
//    0
//   / \
//  1   0
//     / \
//    1   0
//   / \
//  1   1
// ```

type node struct {
	Value int
	Left  *node
	Right *node
}

func isUnival(n *node, value int) bool {
	if n == nil {
		return true
	}

	if n.Value == value {
		return isUnival(n.Left, value) && isUnival(n.Right, value)
	}

	return false
}

func countUnival(n *node) int {
	if n == nil {
		return 0
	}

	if isUnival(n, n.Value) {
		return countUnival(n.Left) + countUnival(n.Right) + 1
	}

	return countUnival(n.Left) + countUnival(n.Right)
}

func main() {
	// 5 unival subtrees
	n0 := node{0, &node{1, nil, nil}, &node{0, &node{1, &node{1, nil, nil}, &node{1, nil, nil}}, &node{0, nil, nil}}}
	fmt.Printf("Unival count: %v\n", countUnival(&n0))

	// 4 unival subtrees
	n1 := node{0, &node{1, nil, nil}, &node{0, &node{0, &node{1, nil, nil}, &node{1, nil, nil}}, &node{0, nil, nil}}}
	fmt.Printf("Unival count: %v\n", countUnival(&n1))
}
