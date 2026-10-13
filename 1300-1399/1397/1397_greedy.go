package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

const bitSize = 64 // read numbers as float64

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	num := func() float64 {
		v, _ := strconv.ParseFloat(sc.Text(), bitSize)
		return v
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for sc.Scan() {
		m := 2 * int(num())
		x, y, total := make([]float64, m), make([]float64, m), make([]float64, m)
		for i := 0; i < m; i++ {
			sc.Scan()
			x[i] = num()
			sc.Scan()
			y[i] = num()
		}
		// total[i]: the sum of distances from point i to all the others
		for i := 0; i < m; i++ {
			for j := i + 1; j < m; j++ {
				d := math.Sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]))
				total[i] += d
				total[j] += d
			}
		}
		// a player's score is half the totals of the own points minus the
		// distances to the other colour, which both sides share: take the
		// largest total left, in turns
		sort.Sort(sort.Reverse(sort.Float64Slice(total)))
		diff := 0.0
		for i, t := range total {
			if i%2 == 0 {
				diff += t
			} else {
				diff -= t
			}
		}
		fmt.Fprintf(out, "%.3f\n", math.Abs(diff/2))
	}
}
