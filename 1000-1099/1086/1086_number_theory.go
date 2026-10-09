package main

import (
	"bufio"
	"fmt"
	"os"
)

// the 15000th prime is 163841
const limit = 163842

func main() {
	composite := make([]bool, limit)
	var primes []int
	for p := 2; p < limit; p++ {
		if composite[p] {
			continue
		}
		primes = append(primes, p)
		for q := p * p; q < limit; q += p {
			composite[q] = true
		}
	}
	in := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var k int
	fmt.Fscan(in, &k)
	for ; k > 0; k-- {
		var n int
		fmt.Fscan(in, &n)
		fmt.Fprintln(w, primes[n-1])
	}
}
