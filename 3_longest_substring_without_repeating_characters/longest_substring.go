package main

import "fmt"

func lengthOfLongestSubstring(s string) int {

	charMap := make(map[rune]int)
	max_length := 0
	start := 0

	for i, el := range s {
		if index, ok := charMap[el]; ok && index >= start {
			start = index + 1
		}
		charMap[el] = i
		current_length := (i - start) + 1

		if current_length > max_length {
			max_length = current_length
		}
	}
	return max_length
}

func main() {
	fmt.Println(lengthOfLongestSubstring("pwwkew"))
}
