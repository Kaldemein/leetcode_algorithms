package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	current_pref := strs[0]

	for i := 1; i < len(strs); i++ {
		word := strs[i]

		j := 0
		for j < len(word) && j < len(current_pref) && word[j] == current_pref[j] {
			j++
		}
		current_pref = current_pref[0:j]

	}
	return current_pref

}

func main() {
	fmt.Printf("%s\n", longestCommonPrefix([]string{"ab", "a"}))
}
