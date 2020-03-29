package main

import (
	"fmt"
)

// Good morning! Here's your coding interview problem for today.
// This problem was asked by Jane Street.
// cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
// Given this implementation of cons:
// def cons(a, b):
//     def pair(f):
//         return f(a, b)
//     return pair
// Implement car and cdr.

type pair struct {
	a int
	b int
}

func cons(a int, b int) *pair {
	return &pair{a, b}
}

func car(p *pair) int {
	return p.a
}

func cdr(p *pair) int {
	return p.b
}

func main() {
	p := cons(3, 4)
	fmt.Printf("pair: %v first: %v last:%v\n", p, car(p), cdr(p))
}
