package main

import (
	"fmt"
	"math"
)

func reverse(x int) int {
	total := 0
	isNegative := false
	if x < 0 {
		isNegative = true
		x = int(math.Abs(float64(x)))
	}
	for x > 0 {
		digit := x % 10
		total = total*10 + digit
		x = x / 10
	}
	if isNegative {
		total -= total * 2
	}
	if int(math.Pow(-2, 31)) > total || total > int(math.Pow(2, 31))-1 {
		return 0
	}
	return total
}
func main() {
	fmt.Println(reverse(-321))
}
