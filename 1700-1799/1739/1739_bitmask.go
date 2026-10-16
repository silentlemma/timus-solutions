package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	scale     = 1000
	safe      = 256 * scale
	deodorant = 1
	perfume   = 2
	both      = deodorant | perfume
	inf       = 1 << 30
	downNum   = 3
	downDen   = 4
	upNum     = 11
	upDen     = 10
)

type move struct {
	kind, deodorized, perfumed, set int
}

var moves []move

// keep the sets not inside another one: carrying more costs nothing,
// since fruit already outside can be brought back and carried again
func addMaximal(sets []int, kind, i, j int) {
	sort.SliceStable(sets, func(a, b int) bool {
		return bits.OnesCount(uint(sets[a])) > bits.OnesCount(uint(sets[b]))
	})
	var kept []int
	for _, a := range sets {
		inside := false
		for _, b := range kept {
			if a&b == a {
				inside = true
				break
			}
		}
		if !inside {
			kept = append(kept, a)
			moves = append(moves, move{kind, i, j, a})
		}
	}
}

func names(set, n int) string {
	var list []string
	for k := 0; k < n; k++ {
		if set>>k&1 == 1 {
			list = append(list, strconv.Itoa(k+1))
		}
	}
	return strconv.Itoa(len(list)) + " " + strings.Join(list, " ")
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	// aromas times 1000 keep 3/4, 11/10 and both together whole
	w := make([]int, n)
	for i := range w {
		fmt.Fscan(in, &w[i])
		w[i] *= scale
	}
	full := 1<<n - 1
	total := make([]int, full+1)
	for m := 1; m <= full; m++ {
		total[m] = total[m&(m-1)] + w[bits.TrailingZeros(uint(m))]
	}
	collect := func(need, change int) []int {
		var sets []int
		for m := 1; m <= full; m++ {
			if m&need == need && (total[m]+change)%safe == 0 {
				sets = append(sets, m)
			}
		}
		return sets
	}
	addMaximal(collect(0, 0), 0, -1, -1)
	// what each spray adds to the total of a set holding the fruit
	weaker := make([]int, n)
	stronger := make([]int, n)
	for i := range w {
		weaker[i] = w[i]*downNum/downDen - w[i]
		stronger[i] = w[i]*upNum/upDen - w[i]
	}
	for i := 0; i < n; i++ {
		addMaximal(collect(1<<i, weaker[i]), deodorant, i, -1)
		addMaximal(collect(1<<i, stronger[i]), perfume, -1, i)
		for j := 0; j < n; j++ {
			change := weaker[i] + stronger[j]
			if i == j {
				change = w[i]*downNum*upNum/(downDen*upDen) - w[i]
			}
			addMaximal(collect(1<<i|1<<j, change), both, i, j)
		}
	}
	// best[used][mask]: fewest exits that get the fruit of mask out
	var best, choice [both + 1][]int
	for used := range best {
		best[used] = make([]int, full+1)
		choice[used] = make([]int, full+1)
		for m := 1; m <= full; m++ {
			best[used][m] = inf
		}
	}
	for mask := 1; mask <= full; mask++ {
		for used := 0; used <= both; used++ {
			for k, mv := range moves {
				if mv.kind&used != 0 || mv.set&mask == 0 {
					continue
				}
				if value := best[used|mv.kind][mask&^mv.set] + 1; value < best[used][mask] {
					best[used][mask] = value
					choice[used][mask] = k
				}
			}
		}
	}
	if best[0][full] >= inf {
		fmt.Fprintln(out, "IMPOSSIBLE")
		return
	}
	var lines []string
	for mask, used := full, 0; mask != 0; {
		mv := moves[choice[used][mask]]
		if back := mv.set &^ mask; back != 0 {
			lines = append(lines, "return "+names(back, n))
		}
		if mv.deodorized >= 0 {
			lines = append(lines, "dearomatize "+strconv.Itoa(mv.deodorized+1))
		}
		if mv.perfumed >= 0 {
			lines = append(lines, "aromatize "+strconv.Itoa(mv.perfumed+1))
		}
		lines = append(lines, "take "+names(mv.set, n))
		used |= mv.kind
		mask &^= mv.set
	}
	fmt.Fprintln(out, len(lines))
	for _, line := range lines {
		fmt.Fprintln(out, line)
	}
}
