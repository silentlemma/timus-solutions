package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var d int64
	if _, err := fmt.Fscan(in, &n, &d); err != nil {
		return
	}
	// sell to everyone who can be served: by the end of month i at most
	// i * d yachts exist, so the running total of sales is capped there
	sales := make([]int64, n)
	var total int64
	for i := 1; i <= n; i++ {
		var a int64
		fmt.Fscan(in, &a)
		next := total + a
		if limit := int64(i) * d; next > limit {
			next = limit
		}
		sales[i-1] = next - total
		total = next
	}
	// build every yacht as late as possible: going backwards, whatever a
	// month cannot build is built earlier and waits one month per boundary
	var carry, storage int64
	for i := n - 1; i >= 0; i-- {
		storage += carry
		carry = sales[i] + carry - d
		if carry < 0 {
			carry = 0
		}
	}
	fmt.Println(total, storage)
}
