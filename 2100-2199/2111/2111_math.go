package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	total := int64(0)
	for i := 0; i < n; i++ {
		var d int64
		fmt.Fscan(in, &d)
		total += d
	}
	// a trip to a city with load L costs L d there and (L - d) d back; summed over
	// any order this is (sum of d)^2, so the order does not matter
	fmt.Println(total * total)
}
