package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

func fits(first, second, height, circumference uint64) bool {
	if first > circumference {
		return false
	}
	if second <= height {
		return true
	}
	area := first * second
	capacity := height * circumference
	if capacity < area {
		return false
	}
	residual := capacity - area
	leftHigh, leftLow := bits.Mul64(residual, residual)
	rightHigh, rightLow := bits.Mul64(first*first, circumference*circumference-first*first)
	return leftHigh > rightHigh || leftHigh == rightHigh && leftLow >= rightLow
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var width, height uint64
	var count int
	fmt.Fscan(input, &width, &height, &count)
	for index := 0; index < count; index++ {
		var cylinderHeight, circumference uint64
		fmt.Fscan(input, &cylinderHeight, &circumference)
		if fits(width, height, cylinderHeight, circumference) ||
			fits(height, width, cylinderHeight, circumference) {
			fmt.Fprintln(output, "Block the hole")
		} else {
			fmt.Fprintln(output, "Too small")
		}
	}
}
