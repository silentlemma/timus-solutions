package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := bufio.NewReader(os.Stdin)
	var depth, position int64
	fmt.Fscan(input, &depth, &position)

	index := position - 1
	pathBits := 0
	for remaining := index; remaining > 0; remaining >>= 1 {
		pathBits++
	}

	leftNumerator, leftDenominator := int64(0), int64(1)
	rightNumerator := int64(1)
	// Leading left moves only increase the right denominator.
	rightDenominator := depth - 1 - int64(pathBits)
	for bit := pathBits - 1; bit >= 0; bit-- {
		if (index>>uint(bit))&1 == 0 {
			rightNumerator += leftNumerator
			rightDenominator += leftDenominator
		} else {
			leftNumerator += rightNumerator
			leftDenominator += rightDenominator
		}
	}

	fmt.Println(leftNumerator+rightNumerator, leftDenominator+rightDenominator)
}
