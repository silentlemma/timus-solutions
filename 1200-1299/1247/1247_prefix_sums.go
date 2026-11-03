package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := bufio.NewReader(os.Stdin)
	var size, limit int
	fmt.Fscan(input, &size, &limit)
	prefix := 0
	// The total excess equals limit. A negative prefix makes the suffix
	// too heavy; a prefix above limit is already a forbidden segment.
	for i := 0; i < size; i++ {
		var value int
		fmt.Fscan(input, &value)
		prefix += value - 1
		if prefix < 0 || prefix > limit {
			fmt.Println("NO")
			return
		}
	}
	fmt.Println("YES")
}
