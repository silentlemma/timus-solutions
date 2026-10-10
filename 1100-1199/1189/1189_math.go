package main

import (
	"fmt"
	"sort"
	"strconv"
)

const (
	base   = 10
	eleven = 11
)

func main() {
	var n int64
	fmt.Scan(&n)
	found := map[int64]bool{}
	// strike digit d at place k from x = (a * 10 + d) * 10^k + b, b < 10^k:
	// then y = a * 10^k + b and x + y = (11a + d) * 10^k + 2b
	for power := int64(1); power <= n; power *= base {
		for carry := int64(0); carry < 2; carry++ {
			twice := n%power + carry*power
			if twice%2 == 0 && twice/2 < power {
				b, q := twice/2, (n-twice)/power
				a, d := q/eleven, q%eleven
				x := (a*base+d)*power + b
				// x has at least two digits and starts with a nonzero digit
				if d < base && x >= base && (a > 0 || d > 0) {
					found[x] = true
				}
			}
		}
	}
	xs := make([]int64, 0, len(found))
	for x := range found {
		xs = append(xs, x)
	}
	sort.Slice(xs, func(i, j int) bool { return xs[i] < xs[j] })
	fmt.Println(len(xs))
	for _, x := range xs {
		fmt.Printf("%d + %0*d = %d\n", x, len(strconv.FormatInt(x, base))-1, n-x, n)
	}
}
