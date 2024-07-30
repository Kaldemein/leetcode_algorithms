package main

import "fmt"

func isValid(s string) bool {
	openBrackts := []rune{}
	bracketsCouples := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}

	if len(s) == 0 || len(s) == 1 {
		return false
	}

	for _, value := range s {

		if value == '(' || value == '[' || value == '{' {
			openBrackts = append(openBrackts, value)
		} else {
			if value == ')' || value == ']' || value == '}' {
				if len(openBrackts) > 0 && openBrackts[len(openBrackts)-1] == bracketsCouples[value] {
					lastBeacketIndex := len(openBrackts) - 1
					openBrackts = openBrackts[:lastBeacketIndex]
				} else {
					return false
				}
			}
		}

	}
	if len(openBrackts) == 0 {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(isValid("){"))
}
