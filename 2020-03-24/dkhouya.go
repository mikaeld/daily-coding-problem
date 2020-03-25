package main

// Good morning! Here's your coding interview problem for today.
// This problem was recently asked by Google.
// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
// Bonus: Can you do this in one pass?

import (
	"fmt"
	"math/rand"
	"time"
)

func generateSlices(len int, limit int) []int {
	array := make([]int, len, len)
	for i := 0; i < len; i++ {
		array[i] = rand.Intn(limit)
	}

	return array
}

func checkK(array []int, k int) bool {
	found := false

	for i := 0; i < len(array); i++ {
		for idx := i + 1; idx < len(array); idx++ {
			if (array[i] + array[idx]) == k {
				found = true
				break
			}
			if found {
				break
			}
		}
	}
	return found
}

func main() {
	k := 17
	size := 4
	max := 20
	maxTest := 100000

	rand.Seed(time.Now().UTC().UnixNano())

	for i := 0; i < maxTest; i++ {
		array := generateSlices(size, max)
		result := checkK(array, k)
		fmt.Printf("Values:%v\tk: %v\tresult:%v\n", array, k, result)

		if result {
			break
		}
	}
}
