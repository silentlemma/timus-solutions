package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const steps = 100

var (
	mass, purity []float64
	order        []int
)

// goldBefore is the gold, in grams times a thousand, in the first t grams of
// the bars laid out from the poorest to the richest
func goldBefore(t float64) float64 {
	gold := 0.0
	for _, i := range order {
		part := math.Min(mass[i], t)
		if part <= 0 {
			break
		}
		gold += part * purity[i]
		t -= part
	}
	return gold
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	var need, fineness float64
	if _, err := fmt.Fscan(reader, &n, &need, &fineness); err != nil {
		return
	}
	mass = make([]float64, n)
	purity = make([]float64, n)
	total := 0.0
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &mass[i], &purity[i])
		total += mass[i]
		order = append(order, i)
	}
	sort.SliceStable(order, func(a, b int) bool { return purity[order[a]] < purity[order[b]] })
	target := need * fineness
	window := func(s float64) float64 { return goldBefore(s+need) - goldBefore(s) }
	// a window of the needed weight sliding from the poorest end to the
	// richest gains gold steadily, so it hits the target if anything does
	if total < need || window(0) > target || window(total-need) < target {
		fmt.Println("NO")
		return
	}
	low, high := 0.0, total-need
	for step := 0; step < steps; step++ {
		mid := (low + high) / 2
		if window(mid) < target {
			low = mid
		} else {
			high = mid
		}
	}
	start := (low + high) / 2
	take := make([]float64, n)
	left := 0.0
	for _, i := range order {
		right := left + mass[i]
		take[i] = math.Max(0, math.Min(right, start+need)-math.Max(left, start))
		left = right
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprintln(writer, "YES")
	for i := 0; i < n; i++ {
		fmt.Fprintf(writer, "%.10f\n", take[i])
	}
}
