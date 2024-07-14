package main

import "fmt"

func twoSum(nums []int, target int) []int {
	numsMap := make(map[int]int)

	for i, el := range nums {
		index, ok := numsMap[target-el]
		if ok {
			return []int{i, index}
		} else {
			numsMap[el] = i
		}
	}
	return []int{-1}
}

func main() {
	fmt.Println(twoSum([]int{1, 2, 3, 4, 5, 6}, 6))
}
