package main

import "fmt"

const (
	side  = 4
	turns = 4
	half  = side / 2
)

// ring gives the position of each quadrant (top left, top right, bottom
// left, bottom right) in the order a quarter turn moves a square through them
var ring = [2][2]int{{0, 1}, {turns - 1, 2}}

func main() {
	var count [turns]int
	for r := 0; r < side; r++ {
		for c := 0; c < side; c++ {
			var colour int
			fmt.Scan(&colour)
			if colour == 1 {
				count[ring[r/half][c/half]]++
			}
		}
	}
	// every layer holds one square of each colour, one per quadrant; the
	// cube is solved when the colour 1 squares of all layers share a quadrant
	best := side * turns
	for t := 0; t < turns; t++ {
		moves := 0
		for p := 0; p < turns; p++ {
			d := (p - t + turns) % turns
			if turns-d < d {
				d = turns - d
			}
			moves += count[p] * d
		}
		if moves < best {
			best = moves
		}
	}
	fmt.Println(best)
}
