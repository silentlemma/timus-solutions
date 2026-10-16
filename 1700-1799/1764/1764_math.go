package main

import (
	"fmt"
	"math/bits"
	"strings"
)

const (
	routes  = 4
	bridges = 6
)

// pairs: each bridge lies on exactly two of the four routes, one pair per
// bridge, in the input order: Nizhny Novgorod, Kotelnich, Perm, Kazan,
// Vyatskiye Polyany, Sarapul
var pairs = [bridges][2]int{{0, 3}, {0, 2}, {2, 3}, {1, 2}, {1, 3}, {0, 1}}

type constraint struct {
	a []int64
	b int64
}

// det is the determinant of a small integer matrix, expanded along the
// first row
func det(rows [][]int64) int64 {
	n := len(rows)
	if n == 1 {
		return rows[0][0]
	}
	var total int64
	for j := 0; j < n; j++ {
		if rows[0][j] == 0 {
			continue
		}
		var minor [][]int64
		for r := 1; r < n; r++ {
			var row []int64
			for c := 0; c < n; c++ {
				if c != j {
					row = append(row, rows[r][c])
				}
			}
			minor = append(minor, row)
		}
		sign := int64(1)
		if j%2 == 1 {
			sign = -1
		}
		total += sign * rows[0][j] * det(minor)
	}
	return total
}

func main() {
	var cons []constraint
	for k := 0; k < bridges; k++ {
		var cap int64
		if _, err := fmt.Scan(&cap); err != nil {
			return
		}
		a := make([]int64, routes)
		a[pairs[k][0]], a[pairs[k][1]] = 1, 1
		cons = append(cons, constraint{a, cap})
	}
	for i := 0; i < routes; i++ {
		a := make([]int64, routes)
		a[i] = -1
		cons = append(cons, constraint{a, 0})
	}
	// the best plan is a corner where four constraints are tight; each
	// corner is solved exactly by Cramer's rule, as numerators over a
	// common positive denominator
	total := len(cons)
	bestNum, bestDen := int64(-1), int64(1)
	var best []int64
	for mask := 0; mask < 1<<total; mask++ {
		if bits.OnesCount(uint(mask)) != routes {
			continue
		}
		var chosen []int
		for k := 0; k < total; k++ {
			if mask>>k&1 == 1 {
				chosen = append(chosen, k)
			}
		}
		matrix := make([][]int64, routes)
		for r, k := range chosen {
			matrix[r] = cons[k].a
		}
		den := det(matrix)
		if den == 0 {
			continue
		}
		nums := make([]int64, routes)
		for c := 0; c < routes; c++ {
			swapped := make([][]int64, routes)
			for r := range matrix {
				swapped[r] = append([]int64(nil), matrix[r]...)
				swapped[r][c] = cons[chosen[r]].b
			}
			nums[c] = det(swapped)
		}
		if den < 0 {
			den = -den
			for c := range nums {
				nums[c] = -nums[c]
			}
		}
		ok := true
		for _, con := range cons {
			var lhs int64
			for c := 0; c < routes; c++ {
				lhs += con.a[c] * nums[c]
			}
			if lhs > con.b*den {
				ok = false
			}
		}
		var sum int64
		for _, v := range nums {
			sum += v
		}
		if ok && sum*bestDen > bestNum*den {
			bestNum, bestDen, best = sum, den, nums
		}
	}
	out := make([]string, routes)
	for c := range out {
		out[c] = fmt.Sprintf("%.3f", float64(best[c])/float64(bestDen))
	}
	fmt.Println(strings.Join(out, " "))
}
