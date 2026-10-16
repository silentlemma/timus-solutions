package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	if _, err := fmt.Fscan(reader, &n, &k); err != nil {
		return
	}
	xs, ys := make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &xs[i], &ys[i])
	}
	// a ball of diameter D hits the pins whose centres lie in a strip of
	// width D + 1 along its path, so the narrowest strip holding k centres
	// decides; one side of it runs along two centres, so only those directions
	best := math.Inf(1)
	if k == 1 {
		best = 0
	}
	across := make([]int64, n)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			dx, dy := xs[j]-xs[i], ys[j]-ys[i]
			for t := 0; t < n; t++ {
				across[t] = dx*ys[t] - dy*xs[t]
			}
			sort.Slice(across, func(a, b int) bool { return across[a] < across[b] })
			gap := across[k-1] - across[0]
			for t := 1; t+k <= n; t++ {
				if g := across[t+k-1] - across[t]; g < gap {
					gap = g
				}
			}
			best = math.Min(best, float64(gap)/math.Hypot(float64(dx), float64(dy)))
		}
	}
	// a ball of any size will do when the strip is no wider than a pin
	if best > 1 {
		fmt.Printf("%.10f\n", best-1)
	} else {
		fmt.Println("0.000000")
	}
}
