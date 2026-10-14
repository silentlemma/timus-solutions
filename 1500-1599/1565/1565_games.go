package main

import "fmt"

const (
	shooters = 3
	air      = -1 // a shot into the air
	indexSum = 0 + 1 + 2
	eps      = 1e-12 // survival chances closer than this count as equal
)

type chances [shooters]float64

var acc [shooters]float64
var order [shooters]int

// strongest is the most accurate living opponent of all three; the earlier
// one on a tie
func strongest(shooter int) int {
	best := -1
	for i := 0; i < shooters; i++ {
		if i != shooter && (best < 0 || acc[i] > acc[best]) {
			best = i
		}
	}
	return best
}

// duel: two left, first to shoot: first wins p / (p + q - p q)
func duel(first, second int) chances {
	p, q := acc[first], acc[second]
	var c chances
	c[first] = p / (p + q - p*q)
	c[second] = 1 - c[first]
	return c
}

// afterHit is the duel left after a hit, with the next living shooter first
func afterHit(turn, killed int) chances {
	first := order[(turn+1)%shooters]
	if first == killed {
		first = order[(turn+2)%shooters]
	}
	return duel(first, indexSum-killed-first)
}

// three gives the chances when all three live and order[turn] shoots; A never
// misses, so the shooting stops at A's turn at the latest
func three(turn int) chances {
	shooter := order[turn]
	if shooter == 0 {
		return afterHit(turn, strongest(shooter))
	}
	p := acc[shooter]
	miss := three((turn + 1) % shooters)
	outcomes := map[int]chances{air: miss}
	best := miss[shooter]
	for target := 0; target < shooters; target++ {
		if target == shooter {
			continue
		}
		hit := afterHit(turn, target)
		var mixed chances
		for i := range mixed {
			mixed[i] = p*hit[i] + (1-p)*miss[i]
		}
		outcomes[target] = mixed
		if mixed[shooter] > best {
			best = mixed[shooter]
		}
	}
	// on a tie the strongest opponent is shot, then A, B, C, then the air
	for _, choice := range []int{strongest(shooter), 0, 1, 2, air} {
		if c, ok := outcomes[choice]; ok && c[shooter] >= best-eps {
			return c
		}
	}
	return miss
}

func main() {
	fmt.Scan(&acc[0], &acc[1], &acc[2])
	var total chances
	orders := 0
	for a := 0; a < shooters; a++ {
		for b := 0; b < shooters; b++ {
			if b == a {
				continue
			}
			order = [shooters]int{a, b, indexSum - a - b}
			c := three(0)
			for i := range total {
				total[i] += c[i]
			}
			orders++
		}
	}
	share := 1.0 / float64(orders)
	fmt.Printf("%.5f %.5f %.5f\n", total[0]*share, total[1]*share, total[2]*share)
}
