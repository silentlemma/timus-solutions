package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var nums []uint64
	for {
		var x uint64
		if _, err := fmt.Fscan(reader, &x); err != nil {
			break
		}
		nums = append(nums, x)
	}
	for i := len(nums) - 1; i >= 0; i-- {
		fmt.Fprintf(writer, "%.4f\n", math.Sqrt(float64(nums[i])))
	}
}
