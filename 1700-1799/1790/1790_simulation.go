package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// run is the pedestals lo, lo + 2, ..., hi where the artifact may be,
// empty when lo > hi
type run struct{ lo, hi int }

func (r run) empty() bool { return r.lo > r.hi }

// a touch inside the run leaves a hole that the next move fills again,
// so only a touch at an end shrinks it
func touch(r run, x int) run {
	if r.empty() {
		return r
	}
	if x == r.lo {
		r.lo += 2
	} else if x == r.hi {
		r.hi -= 2
	}
	return r
}

func spread(r run, n int) run {
	if r.empty() {
		return r
	}
	if r.lo > 1 {
		r.lo--
	} else {
		r.lo++
	}
	if r.hi < n {
		r.hi++
	} else {
		r.hi--
	}
	return r
}

func main() {
	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	scanner.Split(bufio.ScanWords)
	next := func() int {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return v
	}
	n, m := next(), next()
	// runs[p] holds the pedestals of parity p
	runs := [2]run{{2, n - n%2}, {1, n - 1 + n%2}}
	for i := 0; i < m; i++ {
		x := next()
		runs[x%2] = touch(runs[x%2], x)
		// every step flips the parity of the pedestal
		runs = [2]run{spread(runs[1], n), spread(runs[0], n)}
	}
	if runs[0].empty() && runs[1].empty() {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
