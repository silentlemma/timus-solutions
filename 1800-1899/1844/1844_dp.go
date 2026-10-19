package main

import (
	"bufio"
	"fmt"
	"os"
)

type step struct {
	call bool
	mage int
}

func readPlan(in *bufio.Reader, length int) []step {
	plan := make([]step, length)
	for i := range plan {
		var sign string
		fmt.Fscan(in, &sign, &plan[i].mage)
		plan[i].call = sign == "+"
	}
	return plan
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var tests int
	fmt.Fscan(in, &tests)
	for ; tests > 0; tests-- {
		var n, m, k int
		fmt.Fscan(in, &n, &m, &k)
		sandro, zagamius := readPlan(in, n), readPlan(in, m)
		// cell (i, j): Sandro has done i steps and Zagamius j; it is taken
		// when both offices hold one mage, and a step is blocked exactly when
		// it leads into a taken cell. Row n + 1 is all taken: no step down.
		taken := make([][]bool, n+2)
		taken[n+1] = make([]bool, m+1)
		for j := range taken[n+1] {
			taken[n+1][j] = true
		}
		withSandro := make([]bool, k+1)
		for i := 0; i <= n; i++ {
			if i > 0 {
				withSandro[sandro[i-1].mage] = sandro[i-1].call
			}
			taken[i] = make([]bool, m+1)
			shared := 0 // mages in both offices
			for j := 0; j <= m; j++ {
				if j > 0 && withSandro[zagamius[j-1].mage] {
					if zagamius[j-1].call {
						shared++
					} else {
						shared--
					}
				}
				taken[i][j] = shared > 0
			}
		}
		reach := make([][]bool, n+1)
		for i := range reach {
			reach[i] = make([]bool, m+1)
		}
		reach[0][0] = true
		stuck := false
		for i := 0; i <= n && !stuck; i++ {
			for j := 0; j <= m; j++ {
				if !reach[i][j] {
					continue
				}
				down := !taken[i+1][j]
				right := j < m && !taken[i][j+1]
				if !down && !right && (i < n || j < m) {
					stuck = true
					break
				}
				if down {
					reach[i+1][j] = true
				}
				if right {
					reach[i][j+1] = true
				}
			}
		}
		if stuck {
			fmt.Fprintln(out, ":-(")
		} else {
			fmt.Fprintln(out, ":-)")
		}
	}
}
