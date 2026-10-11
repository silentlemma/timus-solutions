package main

import (
	"bufio"
	"fmt"
	"os"
)

const never = 1 << 30

var n, hpH, mpH, hpM, v, dH int
var bolt []int

// land is where the monsters stop after moving from square p
func land(p int) int {
	if p-1 < v {
		return 1
	}
	return p - v
}

// strike is the damage of a pack with h hit points that ends its move on p
func strike(h, p int) int {
	if p != 1 {
		return 0
	}
	return (h + hpM - 1) / hpM
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var nM int
	fmt.Fscan(in, &n, &hpH, &mpH, &hpM, &nM, &v, &dH)
	bolt = make([]int, n+1)
	for p := 1; p <= n; p++ {
		fmt.Fscan(in, &bolt[p])
	}
	top := nM * hpM
	// need[m][h][p] is the fewest hit points the hero needs at the start of
	// a turn with m mana against a pack of h hit points on square p; more
	// hit points never hurt, so this number decides every state
	need := make([][][]int, mpH+1)
	for m := range need {
		need[m] = make([][]int, top+1)
		for h := range need[m] {
			need[m][h] = make([]int, n+1)
			for p := range need[m][h] {
				need[m][h][p] = never
			}
		}
	}
	// cost returns the hit points a spell needs: 'L', 'H', or a teleport target
	cost := func(m, h, p int, spell byte, to int) int {
		after := func(h2, p2, heal int) int {
			q := land(p2)
			rest := need[m-1][h2][q]
			if rest == never {
				return never
			}
			req := strike(h2, q) + rest
			if heal == 0 {
				return req
			}
			if req > hpH {
				return never
			}
			return max(1, req-heal)
		}
		switch spell {
		case 'L':
			if h <= bolt[p] {
				return 1
			}
			return after(h-bolt[p], p, 0)
		case 'H':
			return after(h, p, dH)
		}
		return after(h, to, 0)
	}
	for m := 1; m <= mpH; m++ {
		for h := 1; h <= top; h++ {
			for p := 1; p <= n; p++ {
				best := cost(m, h, p, 'L', 0)
				best = min(best, cost(m, h, p, 'H', 0))
				for to := 1; to <= n; to++ {
					best = min(best, cost(m, h, p, 'T', to))
				}
				need[m][h][p] = best
			}
		}
	}
	hp, h, p := hpH, top, n
	if need[mpH][h][p] > hp {
		fmt.Fprintln(out, "DEFEATED")
		return
	}
	fmt.Fprintln(out, "VICTORIOUS")
	// replay: any spell whose need the hero meets keeps the win in reach
	for m := mpH; h > 0; m-- {
		spell, to := byte('L'), 0
		if cost(m, h, p, 'L', 0) > hp {
			spell = 'H'
			if cost(m, h, p, 'H', 0) > hp {
				spell = 'T'
				for to = 1; cost(m, h, p, 'T', to) > hp; to++ {
				}
			}
		}
		switch spell {
		case 'L':
			fmt.Fprintln(out, "L")
			h -= bolt[p]
		case 'H':
			fmt.Fprintln(out, "H")
			hp = min(hpH, hp+dH)
		default:
			fmt.Fprintln(out, "T", to)
			p = to
		}
		if h > 0 {
			p = land(p)
			hp -= strike(h, p)
		}
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
