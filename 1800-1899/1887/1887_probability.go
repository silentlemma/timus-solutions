package main

import "fmt"

const (
	prime  = 11
	digits = 10
)

func main() {
	var n int
	fmt.Scan(&n)
	rows := make([][]int, len("abc")) // the coefficients a, b and c
	for k := range rows {
		rows[k] = make([]int, n)
		for i := range rows[k] {
			fmt.Scan(&rows[k][i])
		}
	}
	a, b, c := rows[0], rows[1], rows[2]
	// chance[r]: probability that the product so far is r modulo 11
	chance := make([]float64, prime)
	chance[1] = 1
	for i := 0; i < n; i++ {
		next := make([]float64, prime)
		for x := 0; x < digits; x++ {
			factor := (a[i]*x*x + b[i]*x + c[i]) % prime
			for r := 0; r < prime; r++ {
				next[r*factor%prime] += chance[r] / digits
			}
		}
		chance = next
	}
	p := make([]float64, digits)
	for r := 0; r < prime; r++ {
		p[r%digits] += chance[r]
	}
	for _, q := range p {
		// only positive terms are ever added, so an impossible digit stays 0
		if q == 0 {
			fmt.Println(-1)
			return
		}
	}
	// expected draws from the set of digits seen to all ten: a draw of a
	// missing digit moves on, others repeat; the chance to move on is summed
	// directly so that small probabilities keep their precision
	full := 1<<digits - 1
	expect := make([]float64, full+1)
	for mask := full - 1; mask >= 0; mask-- {
		move, sum := 0.0, 1.0
		for d := 0; d < digits; d++ {
			if mask>>d&1 == 1 {
				continue
			}
			move += p[d]
			sum += p[d] * expect[mask|1<<d]
		}
		expect[mask] = sum / move
	}
	fmt.Printf("%.10f\n", expect[0])
}
