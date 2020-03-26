package main

// Good morning! Here's your coding interview problem for today.
// This problem was asked by Uber.
// Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
// For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
// Follow-up: what if you can't use division?

import (
	"fmt"
)

func multiply(input []int) []int {
	output := make([]int, len(input), len(input))
	tmp := make([]int, len(input), len(input))
	array := make([][]int, len(input), len(input))

	// Fill array of slice
	for i := range input {
		// Get pop i numbers from input slice
		tmp = input[i+1 : len(input)]
		// Push in front the i numbers
		tmp = append(tmp, input[:i]...)
		// Append to slice
		array[i] = append(array[i], tmp[:len(input)-1]...)
	}

	// Multiply
	for i := range output {
		// Set initial state to 1
		output[i] = 1
		for j := range tmp {
			// Multiply all slices
			output[i] = output[i] * array[i][j]
		}
	}

	return output
}

func main() {
	array0 := []int{1, 2, 3, 4, 5}
	array1 := []int{3, 2, 1}

	fmt.Printf("Input:%v Output:%v\n", array0, multiply(array0))
	fmt.Printf("Input:%v Output:%v\n", array1, multiply(array1))
}
