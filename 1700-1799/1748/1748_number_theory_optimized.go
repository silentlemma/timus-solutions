package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const most = 64

var primes = []uint64{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53}
var limit uint64

type entry struct {
	value    uint64
	divisors uint32
}

var records []entry

func grow(index, cap int, value uint64, divisors uint32) {
	at := sort.Search(len(records), func(i int) bool { return records[i].value >= value })
	if at == 0 || records[at-1].divisors < divisors {
		end := at
		// Larger values with no greater count cannot answer any future query.
		for end < len(records) && records[end].divisors <= divisors {
			end++
		}
		oldSize := len(records)
		newSize := oldSize - (end - at) + 1
		if newSize > oldSize {
			records = append(records, entry{})
		}
		copy(records[at+1:], records[end:oldSize])
		records = records[:newSize]
		records[at] = entry{value, divisors}
	}
	if index == len(primes) {
		return
	}
	for exponent := 1; exponent <= cap; exponent++ {
		if value > limit/primes[index] {
			break
		}
		value *= primes[index]
		grow(index+1, exponent, value, divisors*uint32(exponent+1))
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var tests int
	fmt.Fscan(in, &tests)
	queries := make([]uint64, tests)
	for i := range queries {
		fmt.Fscan(in, &queries[i])
		if queries[i] > limit {
			limit = queries[i]
		}
	}
	grow(0, most, 1, 1)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, query := range queries {
		at := sort.Search(len(records), func(i int) bool { return records[i].value > query }) - 1
		fmt.Fprintln(out, records[at].value, records[at].divisors)
	}
}
