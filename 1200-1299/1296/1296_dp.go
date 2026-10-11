package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int64 {
		in.Scan()
		x, _ := strconv.Atoi(in.Text())
		return int64(x)
	}
	n := next()
	// best is the largest segment sum so far (the empty segment gives 0), and
	// ending is the largest sum of a segment that ends at the current number
	var best, ending int64
	for i := int64(0); i < n; i++ {
		p := next()
		ending += p
		if ending < 0 {
			ending = 0
		}
		if ending > best {
			best = ending
		}
	}
	fmt.Println(best)
}
