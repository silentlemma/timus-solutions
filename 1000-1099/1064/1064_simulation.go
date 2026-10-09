package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxN = 10000

// steps is the number of comparisons after which the search over n elements
// reaches index target, when every other element sends it towards the target
func steps(n, target int) int {
	p, q := 0, n-1
	for count := 1; p <= q; count++ {
		i := (p + q) / 2
		if i == target {
			return count
		}
		if target < i {
			q = i - 1
		} else {
			p = i + 1
		}
	}
	return 0
}

func main() {
	var target, l int
	fmt.Scan(&target, &l)
	// any array whose elements before the target are smaller and after it are
	// larger leads the search there, so only n decides the number of steps
	var runs [][2]int
	for n := target + 1; n <= maxN; n++ {
		if steps(n, target) != l {
			continue
		}
		if len(runs) > 0 && runs[len(runs)-1][1] == n-1 {
			runs[len(runs)-1][1] = n
		} else {
			runs = append(runs, [2]int{n, n})
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fprintln(w, len(runs))
	for _, r := range runs {
		fmt.Fprintln(w, r[0], r[1])
	}
}
