package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxc = 64 // binomials needed only up to 41

var binom [maxc][maxc]int64

// spread counts ways to put identical items into runs in order, runs may
// stay empty
func spread(items, runs int) int64 {
	if runs == 0 {
		if items == 0 {
			return 1
		}
		return 0
	}
	return binom[items+runs-1][runs-1]
}

func bit(c byte) int {
	if c == 'B' {
		return 1
	}
	return 0
}

func main() {
	for i := 0; i < maxc; i++ {
		binom[i][0] = 1
		for j := 1; j <= i; j++ {
			binom[i][j] = binom[i-1][j-1] + binom[i-1][j]
		}
	}
	in := bufio.NewReader(os.Stdin)
	var n, k int
	var loco string
	fmt.Fscan(in, &n, &k, &loco)
	var have [2][2]int // have[x][y]: carriages with couplings x, y (0 = A)
	for i := 0; i < n; i++ {
		var car string
		fmt.Fscan(in, &car)
		have[bit(car[0])][bit(car[1])]++
	}
	// the train starts with the coupling that fits the locomotive's right
	// end and finishes with the one that fits its left end
	start, end := bit(loco[1]), bit(loco[0])
	var total int64
	for sw := 0; sw <= k; sw++ {
		// AB and BA carriages must alternate, beginning with the one that
		// leaves the starting coupling
		if (sw+1)/2 > have[start][1-start] || sw/2 > have[1-start][start] {
			continue
		}
		if last := start ^ (sw % 2); last != end {
			continue
		}
		// the runs between switches hold the AA and BB carriages
		var runs [2]int
		runs[start], runs[1-start] = sw/2+1, (sw+1)/2
		for aa := 0; aa <= k-sw; aa++ {
			bb := k - sw - aa
			if aa <= have[0][0] && bb <= have[1][1] {
				total += spread(aa, runs[0]) * spread(bb, runs[1])
			}
		}
	}
	if total > 0 {
		fmt.Printf("YES\n%d\n", total)
	} else {
		fmt.Println("NO")
	}
}
