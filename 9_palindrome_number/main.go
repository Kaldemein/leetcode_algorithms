package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	number := strconv.Itoa(x)
	left := 0
	right := len(number) - 1

	for left <= right {
		if number[left] != number[right] {
			return false
		}
		left += 1
		right -= 1
	}
	return true
}

func main() {
	fmt.Printf("%t\n", isPalindrome(10))
}
