package main

import (
	"fmt"
	"sort"
)

// Good morning! Here's your coding interview problem for today.
// This problem was asked by Stripe.
// Given an array of integers, find the first missing positive integer in linear time and constant space.
// In other words, find the lowest positive integer that does not exist in the array. The array can contain
// duplicates and negative numbers as well.

// For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

// You can modify the input array in-place.

func findLowestPos(array []int) int {
	// Sort
	sort.Ints(array)
	// Init to last possible value
	value := array[len(array)-1] + 1

	for i := 0; i < len(array)-1; i++ {
		// Check negative
		if array[i] <= 0 {
			continue
		}

		//Check diff
		if (array[i+1] - array[i]) > 1 {
			// Value found
			value = array[i] + 1
			break
		}
	}

	return value
}

func main() {
	array1 := []int{3, 4, -1, 1}
	array2 := []int{1, 2, 0}
	array3 := []int{1, 1, -1, 3, 5, 6, 7, 10, 3}
	array4 := []int{-1, -2, -3}
	array5 := []int{-1, -2, -3, 0}

	fmt.Printf("array: %v value: %v\n", array1, findLowestPos(array1))
	fmt.Printf("array: %v value: %v\n", array2, findLowestPos(array2))
	fmt.Printf("array: %v value: %v\n", array3, findLowestPos(array3))
	fmt.Printf("array: %v value: %v\n", array4, findLowestPos(array4))
	fmt.Printf("array: %v value: %v\n", array5, findLowestPos(array5))
}
