package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	if _, err := fmt.Fscan(reader, &n, &k); err != nil {
		return
	}
	broken := make([]bool, n)
	for i := 0; i < k; i++ {
		var x int
		fmt.Fscan(reader, &x)
		broken[x-1] = true
	}
	var primes []int
	m := n
	for d := 2; d*d <= m; d++ {
		if m%d == 0 {
			primes = append(primes, d)
			for m%d == 0 {
				m /= d
			}
		}
	}
	if m > 1 {
		primes = append(primes, m)
	}
	// a balanced set of tips is a union of disjoint regular p-gons and q-gons,
	// and blades n / (p q) apart form a p by q grid whose rows are the q-gons
	// and whose columns are the p-gons
	p, q := primes[0], 1
	if len(primes) > 1 {
		q = primes[1]
	}
	classes := n / (p * q)
	var remove []int
	for base := 0; base < classes; base++ {
		badRow, badCol := make([]bool, p), make([]bool, q)
		rows, cols := 0, 0
		for t := 0; t < p*q; t++ {
			if !broken[base+t*classes] {
				continue
			}
			if !badRow[t%p] {
				rows++
			}
			if !badCol[t%q] {
				cols++
			}
			badRow[t%p], badCol[t%q] = true, true
		}
		if rows == 0 {
			continue
		}
		// a row and a column always share a cell, so the kept blades are
		// either all clean rows or all clean columns, whichever hold more, and
		// with one prime the rows are single blades that never balance
		byRows := q > 1 && (p-rows)*q >= (q-cols)*p
		for t := 0; t < p*q; t++ {
			c := base + t*classes
			dropped := badCol[t%q]
			if byRows {
				dropped = badRow[t%p]
			}
			if dropped && !broken[c] {
				remove = append(remove, c+1)
			}
		}
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	if len(remove)+k == n {
		fmt.Fprintln(writer, -1)
		return
	}
	fmt.Fprintln(writer, len(remove))
	for i, x := range remove {
		if i > 0 {
			writer.WriteByte(' ')
		}
		writer.WriteString(strconv.Itoa(x))
	}
	writer.WriteByte('\n')
}
