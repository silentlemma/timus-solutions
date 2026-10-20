package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	input := bufio.NewReader(os.Stdin)
	var x, y string
	fmt.Fscan(input, &x, &y)
	size := len(x)
	if len(y) > size {
		size = len(y)
	}
	x = strings.Repeat("0", size-len(x)) + x
	y = strings.Repeat("0", size-len(y)) + y

	propagating, longest := 0, 0
	for i := 0; i < size; i++ {
		if x[i] != y[i] {
			propagating++
		} else {
			// A common one starts a carry through the differing bits above it.
			if x[i] == '1' && propagating+1 > longest {
				longest = propagating + 1
			}
			propagating = 0
		}
	}
	// Include the initial call and the final call with a zero second argument.
	fmt.Println(longest + 2)
}
