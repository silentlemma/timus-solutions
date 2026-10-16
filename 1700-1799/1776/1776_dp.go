package main

import "fmt"

const (
	seconds = 10
	// sure: once a whole line is done with this certainty the rest of the
	// sum is lost in rounding
	sure = 1e-15
)

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	m := n - 2
	// done[i]: the chance that i rockets between two launched ones are all
	// launched within the volleys counted so far; a stretch of i rockets
	// splits at a random one into stretches of l and i - 1 - l
	done := make([]float64, m+1)
	done[0] = 1
	volleys := 0.0
	for j := 1; j <= m; j++ {
		volleys += 1 - done[m]
		before := append([]float64(nil), done...)
		for i := 0; i <= m; i++ {
			if i <= j {
				done[i] = 1
				continue
			}
			sum := 0.0
			for l := 0; l < i; l++ {
				sum += before[l] * before[i-1-l]
			}
			done[i] = sum / float64(i)
		}
		if 1-done[m] < sure {
			break
		}
	}
	fmt.Printf("%.11f\n", seconds*volleys)
}
