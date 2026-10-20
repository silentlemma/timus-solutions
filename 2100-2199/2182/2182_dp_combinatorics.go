package main

import (
	"bufio"
	"math/bits"
	"os"
	"strconv"
)

const (
	small    = 60 // only boxes up to the number of bits can receive extra bottles
	wordBits = 64
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	next := func() uint64 {
		scanner.Scan()
		value, _ := strconv.ParseUint(scanner.Text(), 10, wordBits)
		return value
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	n, q := int(next()), int(next())
	binom := make([][]uint64, n+1)
	for i := range binom {
		binom[i] = make([]uint64, n+1)
		binom[i][0] = 1
		for j := 1; j <= i; j++ {
			binom[i][j] = binom[i-1][j-1] + binom[i-1][j]
		}
	}
	top := uint64(1)<<uint(n) - 1
	last := small
	if top < small {
		last = int(top)
	}
	// Box k gets one bottle for every bottle placed in a box j != k with
	// popcount(j) = k; boxes above 60 hold only their own one, and the small
	// boxes are filled from the top down, as popcount(j) < j for j > 1.
	count := make([]uint64, last+1)
	for k := last; k >= 1; k-- {
		total := uint64(1)
		if k <= n {
			total += binom[n][k]
		}
		if k == 1 {
			total--
		}
		for j := k + 1; j <= last; j++ {
			if bits.OnesCount(uint(j)) == k {
				total += count[j] - 1
			}
		}
		count[k] = total
	}
	for i := 0; i < q; i++ {
		a := next()
		if i > 0 {
			writer.WriteByte(' ')
		}
		if a <= uint64(last) {
			writer.WriteString(strconv.FormatUint(count[a], 10))
		} else {
			writer.WriteByte('1')
		}
	}
	writer.WriteByte('\n')
}
