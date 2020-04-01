package main

import (
	"fmt"
)

// Good morning! Here's your coding interview problem for today.

// This problem was asked by Airbnb.

// Given a list of integers, write a function that returns the largest sum
// of non-adjacent numbers. Numbers can be `0` or negative.

// For example, `[2, 4, 6, 2, 5]` should return 13, since we pick `2`, `6`,
//  and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

// Follow-up: Can you do this in O(N) time and constant space?
func getMaxSum(array []int) int {
	maxSum := 0

	for idx := 0; idx < len(array); idx++ {
		for hop := len(array); hop > 1; hop-- {
			tmpSum := generateSeqSum(array, idx, hop)
			if maxSum < tmpSum {
				maxSum = tmpSum
			}
		}
	}

	return maxSum
}

func generateSeqSum(array []int, idx int, hop int) int {

	if hop == 0 {
		return array[idx]
	}

	// First side check
	sum := 0
	for i := idx; i < len(array); i += hop {
		sum += array[i]
	}

	//Reverse slice
	for i, j := 0, len(array)-1; i < j; i, j = i+1, j-1 {
		array[i], array[j] = array[j], array[i]
	}

	// Reverse check
	sumRev := 0
	for i := idx; i < len(array); i += hop {
		sumRev += array[i]
	}

	if sum > sumRev {
		return sum
	}

	return sumRev
}

func main() {
	array0 := []int{2, 4, 6, 2, 5}
	fmt.Printf("Sum %v\n", getMaxSum(array0))

	array1 := []int{5, 1, 1, 5}
	fmt.Printf("Sum %v\n", getMaxSum(array1))

	array2 := []int{-7, 5, 1, 3, 20}
	fmt.Printf("Sum %v\n", getMaxSum(array2))
}
