package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	limit = uint64(1_000_000_000_000_000_000)
	most  = 64
)

var primes = []uint64{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53}

type entry struct {
	value    uint64
	divisors int64
}

var found []entry

// the smallest number with a given set of exponents puts the largest
// exponents on the smallest primes, so only numbers 2^a 3^b 5^c ... with
// a >= b >= c >= ... can be answers
func grow(index, cap int, value uint64, divisors int64) {
	found = append(found, entry{value, divisors})
	if index == len(primes) {
		return
	}
	for e := 1; e <= cap; e++ {
		if value > limit/primes[index] {
			break
		}
		value *= primes[index]
		grow(index+1, e, value, divisors*int64(e+1))
	}
}

func main() {
	grow(0, most, 1, 1)
	sort.Slice(found, func(i, j int) bool { return found[i].value < found[j].value })
	values := make([]uint64, len(found))
	best := make([]entry, len(found))
	top := entry{0, 0}
	for i, f := range found {
		if f.divisors > top.divisors {
			top = f
		}
		values[i] = f.value
		best[i] = top
	}
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var n uint64
		fmt.Fscan(in, &n)
		k := sort.Search(len(values), func(i int) bool { return values[i] > n }) - 1
		fmt.Fprintln(out, best[k].value, best[k].divisors)
	}
}
