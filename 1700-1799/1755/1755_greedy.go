package main

import "fmt"

type good struct {
	worth, cost, amount int64
	slot                int
}

func main() {
	var a1, b1, a2, b2, n, m int64
	if _, err := fmt.Scan(&a1, &b1, &a2, &b2, &n, &m); err != nil {
		return
	}
	// Karlsson leaves the piece he likes no more than half, so the best is
	// the piece of greatest worth to Little Boy within half of Karlsson's total:
	// a fractional knapsack where each ingredient is taken by worth per cost
	goods := []good{{a1, a2, n, 0}, {b1, b2, m, 1}}
	// zero-cost goods first, then by worth over cost, highest first
	if goods[1].worth*goods[0].cost > goods[0].worth*goods[1].cost {
		goods[0], goods[1] = goods[1], goods[0]
	}
	room := float64(a2*n+b2*m) / 2
	piece := make([]float64, len(goods))
	for _, g := range goods {
		take := float64(g.amount)
		if float64(g.cost*g.amount) > room {
			take = room / float64(g.cost)
		}
		piece[g.slot] = take
		room -= take * float64(g.cost)
	}
	fmt.Printf("%.8f %.8f\n", piece[0], piece[1])
}
