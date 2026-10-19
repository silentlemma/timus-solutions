package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// times in units of 1/50 s: a car (20 km/h) covers a metre in 9 units and
// Egor (5 km/h) crosses a 2 m lane in 72
const (
	metre = 9
	lane  = 72
	car   = 5
	units = 50.0
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	type span struct{ low, high int }
	blocked := []span{}
	// a car is on the crossing from metre d to metre (d + car); a start time
	// s is bad when Egor's time in the car's lane overlaps that
	for side := 0; side < 2; side++ {
		var count int
		fmt.Fscan(reader, &count)
		for i := 0; i < count; i++ {
			var d int
			fmt.Fscan(reader, &d)
			enter := side * lane
			blocked = append(blocked, span{metre*d - enter - lane, metre*(d+car) - enter})
		}
	}
	sort.Slice(blocked, func(i, j int) bool { return blocked[i].low < blocked[j].low })
	start := 0
	for _, b := range blocked {
		if b.low >= start {
			break
		}
		if b.high > start {
			start = b.high
		}
	}
	fmt.Printf("%.6f\n", float64(start)/units)
}
