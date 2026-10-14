package main

import "fmt"

// narrowestFactor gives four times the square of the shortest longest chord
// of a cover of side or radius 1: a circle's diameter, a square's side, a
// triangle's height
var narrowestFactor = []int{0, 16, 4, 3}

// widestFactor gives four times the square of the longest segment in a hole:
// a circle's diameter, a square's diagonal, a triangle's side
var widestFactor = []int{0, 16, 8, 4}

func main() {
	var kind, size, n int
	fmt.Scan(&kind, &size, &n)
	hole := widestFactor[kind] * size * size
	count := 0
	// a cover held upright crosses the plane of the hole along parallel chords,
	// so it passes when its longest chord in some direction fits in the hole
	for i := 0; i < n; i++ {
		fmt.Scan(&kind, &size)
		if narrowestFactor[kind]*size*size <= hole {
			count++
		}
	}
	fmt.Println(count)
}
