package main

import "fmt"

// compare function finds the longest palindrome centered at left and right indices
func compare(left, right int, s string, lngstPal *[]rune) {
	for left >= 0 && right < len(s) && rune(s[left]) == rune(s[right]) {
		// Prepend left character
		*lngstPal = append([]rune{rune(s[left])}, *lngstPal...)
		// Append right character
		*lngstPal = append(*lngstPal, rune(s[right]))

		left--
		right++
	}
}

func longestPalindrome(s string) string {
	var lngstPal []rune
	for i, ch := range s {
		var currPal []rune

		// Odd case
		currPal = []rune{ch}
		compare(i-1, i+1, s, &currPal)
		if len(lngstPal) < len(currPal) {
			lngstPal = make([]rune, len(currPal))
			copy(lngstPal, currPal)
		}

		// Even case
		currPal = []rune{}
		compare(i, i+1, s, &currPal)
		if len(lngstPal) < len(currPal) {
			lngstPal = make([]rune, len(currPal))
			copy(lngstPal, currPal)
		}
	}

	return string(lngstPal)
}

func main() {
	fmt.Printf("%s\n", longestPalindrome("aaaa"))
}
